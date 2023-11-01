
<div align="center">
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/written_by-GPT-green">
    </a>
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/could_be-Wrong-red">
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

To use the module, you need to provide the necessary command-line arguments. The `main` module in `gpt_readme/__main__.py` serves as the entry point. You can run the module with the following command:

```
python -m gpt_readme
```

Make sure to configure the necessary environment variables before running the module.

## Features

The `gpt_readme` module consists of the following files and submodules:

- `gpt_readme/__init__.py`: Defines metadata about the `gpt_readme` library, such as version, author, and URL.

- `gpt_readme/__main__.py`: Serves as the entry point for the `gpt_readme` codebase.

- `gpt_readme/constants.py`: Defines constants and variables used in the codebase, including environment variables, a console object, and mappings between file extensions and programming languages.

- `gpt_readme/dir_summary.py`: Generates a summary of a directory and its contents. It recursively traverses the directory structure, collects file and module summaries, and generates the final summary using the GPT-3.5-turbo model.

- `gpt_readme/file_summary.py`: Generates a summary of a given file. It logs the file path, retrieves the content of the file, determines the language of the file, and generates a summary using the GPT-3.5-turbo model.

- `gpt_readme/main.py`: Generates a README file for a code repository or file. It parses command-line arguments, generates summaries of code modules and their content using the `dir_summary` and `file_summary` functions, calls the `prompt_summary` function to generate a summary using the GPT-3.5-turbo model, and writes the generated README to a file.

- `gpt_readme/prompts.py`: Contains predefined prompts in Chinese for generating documentation for code modules or files. It provides instructions on how to structure the documentation and placeholders for relevant information.

- `gpt_readme/utils.py`: Provides utility functions for working with files and generating prompts and summaries. It includes functions for file handling, language detection, and prompt/summary construction.

## Acknowledgement

The `gpt_readme` module relies on the following third-party libraries:

- OpenAI GPT-3.5-turbo: A language model used for generating code summaries and documentation.

I would like to express my gratitude to the developers of the OpenAI GPT-3.5-turbo for their contribution to this module.
