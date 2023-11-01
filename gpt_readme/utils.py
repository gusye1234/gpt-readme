import os
from .constants import scan_exts, ext2language


def generate_end(chunk):
    if chunk['choices'][0]['finish_reason'] != None:
        return True


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
