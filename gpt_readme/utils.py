import os
import json
import hashlib
from getpass import getpass
from . import constants
from .constants import scan_exts, ext2language, console


def setup_env(args):
    if os.environ.get('OPENAI_API_KEY', None) is None:
        os.environ['OPENAI_API_KEY'] = getpass("Your OpenAI API key: ")
    local_path = os.path.relpath(args.path)
    constants.envs['human_language'] = args.language
    if args.cache:
        constants.envs['cache'] = get_cache_config(local_path)
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
    if chunk['choices'][0]['finish_reason'] != None:
        return True


def get_cache_config(path):
    if os.path.isfile(path):
        cache_path = os.path.join(os.path.pardir(path), ".gpt_readme.json")
    else:
        cache_path = os.path.join(path, ".gpt_readme.json")
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
        cache_path = os.path.join(os.path.pardir(path), ".gpt_readme.json")
    else:
        cache_path = os.path.join(path, ".gpt_readme.json")
    with open(cache_path, 'w') as f:
        json.dump(cache, f)


def hash_content(content: str):
    content = content.strip()
    return hashlib.md5(content.encode()).hexdigest()


def get_language(path):
    ext = os.path.splitext(path)[-1][1:]
    return ext2language[ext]


def ignore_dir(path):
    path = os.path.basename(path)
    if path.startswith("."):
        return True
    if path.startswith("__"):
        return True
    return False


def ignore_file(path):
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
