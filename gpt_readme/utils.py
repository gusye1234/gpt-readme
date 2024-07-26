import os
import json
import hashlib
import inspect
import asyncio
from functools import wraps
from rich.prompt import Confirm
from . import constants
from .constants import scan_exts, ext2language, console
from gitignore_parser import parse_gitignore


def setup_env(args):
    if not args.agree:
        is_openai_ok = Confirm.ask(
            "gpt-readme use OpenAI API. By continuing, you agree to send your code to OpenAI:",
            default=True,
        )
        if not is_openai_ok:
            exit(0)
    local_path = os.path.relpath(args.path)
    abs_path = os.path.abspath(args.path)
    constants.envs["human_language"] = args.language
    constants.envs["root_path"] = local_path
    constants.envs["gpt_model"] = args.model
    constants.envs["max_dir_entity"] = args.max_dir_entity
    if args.cache:
        constants.envs["cache"] = get_cache_config(local_path)

    constants.envs["gitignore_matcher"] = None
    if os.path.exists(os.path.join(abs_path, ".gitignore")):
        console.log("Found .gitignore file")
        constants.envs["gitignore_matcher"] = parse_gitignore(
            os.path.join(abs_path, ".gitignore")
        )
    for ext in args.exts.split(","):
        ext = ext.strip()
        if not ext:
            continue
        if ext in ext2language:
            scan_exts.append(ext)
        else:
            console.log(
                f"Extension [{ext}] is not supported yet, please use one of [{','.join(ext2language.keys())}]"
            )


def end_env(args):
    local_path = os.path.relpath(args.path)
    if args.cache:
        set_cache_config(local_path, constants.envs["cache"])


def generate_end(chunk):
    if chunk["choices"][0]["finish_reason"] != None:
        return True


def relative_module(path):
    basedir = os.path.basename(constants.envs["root_path"])
    return path.replace(constants.envs["root_path"], basedir)


def get_cache_config(path):
    if os.path.isfile(path):
        cache_path = os.path.join(os.path.dirname(path), ".gpt-readme.json")
    else:
        cache_path = os.path.join(path, ".gpt-readme.json")
    if os.path.exists(cache_path):
        try:
            with open(cache_path) as f:
                caches = json.load(f)
            return caches
        except:
            return {}
    else:
        return {}


def set_cache_config(path, cache):
    if os.path.isfile(path):
        cache_path = os.path.join(os.path.dirname(path), ".gpt-readme.json")
    else:
        cache_path = os.path.join(path, ".gpt-readme.json")
    with open(cache_path, "w") as f:
        json.dump(cache, f)


def hash_content(content: str):
    content = content.strip()
    return hashlib.md5(content.encode()).hexdigest()


def hash_dir(path):
    paths = sorted(list(os.listdir(path)))
    name_hash_in_order = []
    for entity in paths:
        real_path = os.path.join(path, entity)
        if os.path.isfile(real_path):
            if ignore_file(real_path):
                continue
            content = get_file_content(real_path)
            content = "".join(content)
            name_hash_in_order.append((real_path, hash_content(content)))
        elif not ignore_dir(real_path):
            name_hash_in_order.append((real_path, hash_dir(real_path)))
    return hashlib.md5(str(name_hash_in_order).encode()).hexdigest()


def get_language(path):
    ext = os.path.splitext(path)[-1][1:]
    return ext2language[ext]


def ignore_dir(path):
    abs_path = os.path.abspath(path)
    if constants.envs["gitignore_matcher"] is not None:
        if constants.envs["gitignore_matcher"](abs_path):
            return True
    path = os.path.basename(path).strip()
    if path.startswith(".") and path.strip(".") != "":
        return True
    return False


def ignore_file(path):
    abs_path = os.path.abspath(path)
    if constants.envs["gitignore_matcher"] is not None:
        if constants.envs["gitignore_matcher"](abs_path):
            return True
    name = os.path.basename(path)
    if name.startswith("."):
        return True
    ext = os.path.splitext(path)[-1][1:]
    return ext not in scan_exts


def get_file_content(path):
    res = []
    with open(path) as f:
        res.extend(f.readlines())
    return res


def construct_prompt(system, user):
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def construct_summary_pair(pairs: dict):
    res = ""
    for key, value in pairs.items():
        summary = f"# {key}\n{value}\n\n"
        res += summary
    return res


def limit_async_func_call(max_size=8, wait_after_seconds=0.01):
    """Add restriction of maximum async calling times for a async func"""

    def final_decro(func):
        assert inspect.iscoroutinefunction(func), "func must be a coroutine function"
        current_running = 0

        @wraps(func)
        async def wait_func(*args, **kwargs):
            nonlocal current_running
            while True:
                if current_running < max_size:
                    current_running += 1
                    break
                await asyncio.sleep(wait_after_seconds)
            try:
                result = await func(*args, **kwargs)
            finally:
                current_running -= 1
            return result

        return wait_func

    return final_decro
