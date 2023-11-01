import os
import openai
import sys
from .utils import (
    ignore_dir,
    ignore_file,
    construct_summary_pair,
    construct_prompt,
    generate_end,
)
from .constants import console, envs
from .file_summary import file_summary
from .prompts import MODULE_PROMPT, SYSTEM_PROMPT


def prompt_summary(**kwargs):
    final_prompt = MODULE_PROMPT.format(**kwargs)
    final_system = SYSTEM_PROMPT.format(**kwargs, human_language=envs['human_language'])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=construct_prompt(final_system, final_prompt),
        stream=True,
    )
    output = ""
    for chunk in response:
        if generate_end(chunk):
            break
        text = chunk['choices'][0]['delta']['content']
        output += text
        console.print(text, end='')
        sys.stdout.flush()
    console.print(end='\r')
    return output


def dir_summary(path):
    console.print(f"[bold green]DIR[/bold green] {path}")
    paths = sorted(list(os.listdir(path)))
    sub_file_summaries = {}
    sub_module_summaries = {}
    total_languages = set()
    for entity in paths:
        real_path = os.path.join(path, entity)
        if os.path.isfile(real_path):
            if ignore_file(real_path):
                continue
            result = file_summary(real_path)
            sub_file_summaries[real_path] = result["content"]
            total_languages.add(result["language"])
        elif not ignore_dir(real_path):
            result = dir_summary(real_path)
            if result["content"] == "":
                continue
            sub_module_summaries[real_path] = result["content"]
            total_languages.add(result["language"])
    if len(sub_file_summaries) == 0 and len(sub_module_summaries) == 0:
        return {"content": "", "language": ""}
    language = " ".join(total_languages)

    # fast forward for single file or module
    if len(sub_file_summaries) == 1 and len(sub_module_summaries) == 0:
        return {"content": list(sub_file_summaries.values())[0], "language": language}
    if len(sub_file_summaries) == 0 and len(sub_module_summaries) == 1:
        return {"content": list(sub_file_summaries.values())[0], "language": language}
    file_summaries = construct_summary_pair(sub_file_summaries)
    module_summaries = construct_summary_pair(sub_module_summaries)
    summary = prompt_summary(
        language=language,
        file_summaries=file_summaries,
        module_summaries=module_summaries,
        max_length=300,
        path=path,
    )
    console.print(summary)
    return {"content": summary, "language": language}
