import os
from openai import AsyncOpenAI
from .utils import limit_async_func_call

if os.environ.get("OPENAI_API_KEY", None) is None:
    from getpass import getpass

    api_key = getpass("Your OpenAI API key: ")
else:
    api_key = os.environ["OPENAI_API_KEY"]
openai_async_client = AsyncOpenAI(api_key=api_key)


@limit_async_func_call(max_size=12)
async def openai_complete(model, prompt, system_prompt=None, **kwargs) -> str:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = await openai_async_client.chat.completions.create(
        model=model, messages=messages, **kwargs
    )
    return response.choices[0].message.content
