# import sys
import openai
from .constants import console, envs
from .utils import (
    get_file_content,
    construct_prompt,
    get_language,
    hash_content,
    relative_module,
)
from .prompts import FILE_PROMPT, SYSTEM_PROMPT
from .llm import openai_complete


async def prompt_summary(**kwargs):
    content = kwargs["code"]
    if envs["cache"] is not None:
        file_cache = envs["cache"].get(kwargs["path"], None)
        if file_cache is not None and file_cache["hash"] == hash_content(content):
            console.log(f"[bold green]✓ FILE[/bold green] {kwargs['path']} use cache")
            return file_cache["summary"]
    final_prompt = FILE_PROMPT.format(**kwargs)
    final_system = SYSTEM_PROMPT.format(**kwargs)
    console.log(f"  FILE {kwargs['path']} summary...")

    response = await openai_complete(
        model=envs["gpt_model"],
        prompt=final_prompt,
        system_prompt=final_system,
        temperature=0.1,
    )
    output = response.strip()
    if envs["cache"] is not None:
        envs["cache"][kwargs["path"]] = {}
        envs["cache"][kwargs["path"]]["summary"] = output
        envs["cache"][kwargs["path"]]["hash"] = hash_content(content)
    console.log(f"[bold green]✓ FILE[/bold green] {kwargs['path']} done")
    return output


async def file_summary(file_path):
    module = relative_module(file_path)
    # console.log(f"[bold blue]FILE[/bold blue] {module} running...")
    content = "".join(get_file_content(file_path)).strip()
    language = get_language(file_path)

    if content == "":
        return {"summary": "Empty file", "language": language}
    summary = await prompt_summary(
        language=language, code=content, max_length=200, path=module
    )
    return {"summary": summary, "language": language}
