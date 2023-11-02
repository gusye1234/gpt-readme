import sys
import openai
from .constants import console, envs
from .utils import (
    get_file_content,
    construct_prompt,
    get_language,
    generate_end,
    hash_content,
)
from .prompts import FILE_PROMPT, SYSTEM_PROMPT


def prompt_summary(**kwargs):
    content = kwargs['code']
    if envs["cache"] is not None:
        file_cache = envs["cache"].get(kwargs['path'], None)
        if file_cache is not None and file_cache["hash"] == hash_content(content):
            console.print("[green]Already summarized[/green]")
            return file_cache["summary"]
    final_prompt = FILE_PROMPT.format(**kwargs)
    final_system = SYSTEM_PROMPT.format(**kwargs, human_language=envs['human_language'])
    response = openai.ChatCompletion.create(
        model=kwargs['model'],
        messages=construct_prompt(final_system, final_prompt),
        temperature=0,
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
    if envs["cache"] is not None:
        envs["cache"][kwargs['path']] = {}
        envs["cache"][kwargs['path']]["summary"] = output
        envs["cache"][kwargs['path']]["hash"] = hash_content(content)
    return output


def file_summary(file_path, model):
    console.print(f"[bold blue]FILE[/bold blue] {file_path}")
    content = "".join(get_file_content(file_path)).strip()
    language = get_language(file_path)
    summary = prompt_summary(
        language=language, code=content, max_length=200, path=file_path, model=model
    )
    return {"content": summary, "language": language}
