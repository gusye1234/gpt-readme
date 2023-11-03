<div align="center">
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/written_by-human-green">
    </a>
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/maybe-Right-blue">
    </a>
    <a href="https://pypi.org/project/gpt_readme/">
      <img src="https://img.shields.io/pypi/v/gpt_readme.svg">
    </a>
</div>


# gpt_readme

The `gpt_readme` module is a code library that generates README files for code repositories or files using the OpenAI GPT-3.5-turbo model. It includes several submodules and files that provide different functionalities for generating code summaries and documentation.

## Introduction

The main functionality of the `gpt_readme` module is to generate README files for code repositories or files. It utilizes the OpenAI GPT-3.5-turbo model to summarize the code and create the README. The generated README includes language-specific summaries of modules and their content, making it useful for automatically generating README files for code projects.

## Get Started

To install the `gpt_readme` module, you can use the following command:

```
pip install gpt_readme
```

Or download and install it from source:

```
git clone https://github.com/gusye1234/gpt-readme.git
cd gpt-readme
pip install -e .
```

To use the command line tool, you need to provide the necessary command-line arguments. 

```
# the command to create this repo's readme
>> cd gpt_readme
>> gpt_readme --path="./gpt_readme"
```

You can check the detail options by

```
>> gpt_readme -h
usage: gpt_readme [-h] [--path PATH] [--exts EXTS] [--language LANGUAGE] [--demand DEMAND] [--out OUT] [--model MODEL]

GPT-readme: Use ChatGPT to write README, based on your code.

options:
  -h, --help           show this help message and exit
  --path PATH          The local path for your code repo/file
  --exts EXTS          Select your code extension name, split by comma, e.g. py,cpp
  --language LANGUAGE  Select your readme language
  --demand DEMAND      Additional requires for the gpt-readme
  --out OUT            Select where your readme file should be saved
  --model MODEL        Select which model to use, default is gpt-3.5-turbo
```

Make sure to configure the necessary environment variables (`OPENAI_API_KEY`)before running the module.

## Features

The `gpt_readme` module consists of the following files and submodules:

- `gpt_readme/constants.py`: Defines constants and variables used in the codebase, including environment variables, a console object, and mappings between file extensions and programming languages.

- `gpt_readme/dir_summary.py`: Generates a summary of a directory and its contents. It recursively traverses the directory structure, collects file and module summaries, and generates the final summary using the GPT-3.5-turbo model.

- `gpt_readme/file_summary.py`: Generates a summary of a given file. It logs the file path, retrieves the content of the file, determines the language of the file, and generates a summary using the GPT-3.5-turbo model.

- `gpt_readme/main.py`: Generates a README file for a code repository or file. It parses command-line arguments, generates summaries of code modules and their content using the `dir_summary` and `file_summary` functions, calls the `prompt_summary` function to generate a summary using the GPT-3.5-turbo model, and writes the generated README to a file.

- `gpt_readme/prompts.py`: Contains predefined prompts in Chinese for generating documentation for code modules or files. It provides instructions on how to structure the documentation and placeholders for relevant information.

- `gpt_readme/utils.py`: Provides utility functions for working with files and generating prompts and summaries. It includes functions for file handling, language detection, and prompt/summary construction.

## Acknowledgement

The `gpt_readme` module relies on the following third-party libraries:

- `openai`: OpenAI GPT-3.5-turbo: A language model used for generating code summaries and documentation.
- `rich`: Rich is a Python library for rich text and beautiful formatting in the terminal.
