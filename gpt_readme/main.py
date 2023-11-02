import os
import openai
import argparse
from rich.markdown import Markdown
from .constants import readme_header, console
from . import constants
from .utils import construct_prompt, end_env, setup_env
from .dir_summary import dir_summary
from .file_summary import file_summary
from .prompts import FINAL_PROMPT, SYSTEM_PROMPT


def parse_args():
    parser = argparse.ArgumentParser(
        description='GPT-readme: Use ChatGPT to write README, based on your code.'
    )
    parser.add_argument(
        "--path",
        type=str,
        default="./",
        help='The local path for your code repo/file',
    )
    parser.add_argument(
        "--exts",
        type=str,
        default="py,cpp",
        help='Select your code extension name, split by comma, e.g. py,cpp',
    )
    parser.add_argument(
        "--language",
        type=str,
        default="english",
        help='Select your readme language',
    )
    parser.add_argument(
        "--demand",
        type=str,
        default="No false summary is allowed",
        help='Additional requires for the gpt-readme',
    )
    parser.add_argument(
        "--out",
        type=str,
        default="./readme.md",
        help='Select where your readme file should be saved',
    )
    parser.add_argument(
        "--cache",
        type=bool,
        default=True,
        help='Cache the summary of the code, to speed up the generation of next time. It will leave a .gpt-readme.json file under the path',
    )
    return parser.parse_args()


def prompt_summary(**kwargs):
    final_prompt = FINAL_PROMPT.format(**kwargs)
    final_system = SYSTEM_PROMPT.format(
        **kwargs, human_language=constants.envs['human_language']
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=construct_prompt(final_system, final_prompt),
        temperature=0,
    )
    return response['choices'][0]['message']['content']


def main():
    args = parse_args()
    local_path = os.path.relpath(args.path)

    setup_env(args)
    if os.path.isfile(local_path):
        summaries = file_summary(local_path)
    else:
        summaries = dir_summary(local_path)
    end_env(args)

    console.rule("Generating README")
    readme = prompt_summary(
        language=summaries['language'],
        module_summaries=summaries['summary'],
        path=local_path,
        user_demand=args.demand,
    )
    console.print(Markdown(readme))
    with open(args.out, 'w') as f:
        f.write(readme_header(args))
        f.write(readme)
    console.rule("Done")
