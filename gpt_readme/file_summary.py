import sys
import openai
from .constants import console, envs
from .utils import get_file_content, construct_prompt, get_language, generate_end
from .prompts import FILE_PROMPT, SYSTEM_PROMPT


def prompt_summary(**kwargs):
    final_prompt = FILE_PROMPT.format(**kwargs)
    final_system = SYSTEM_PROMPT.format(**kwargs, human_language=envs['human_language'])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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
    return output


def file_summary(file_path):
    console.print(f"[bold blue]FILE[/bold blue] {file_path}")
    content = "".join(get_file_content(file_path)).strip()
    language = get_language(file_path)
    summary = prompt_summary(
        language=language, code=content, max_length=200, path=file_path
    )
    return {"content": summary, "language": language}
