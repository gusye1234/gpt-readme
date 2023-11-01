
<div align="center">
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/written_in-GPT-green">
    </a>
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/could_be-Wrong-red">
    </a>
    <a href="https://pypi.org/project/gpt_readme/">
      <img src="https://img.shields.io/pypi/v/gpt_readme.svg">
    </a>
</div>

# gpt_readme

The `gpt_readme` module is a Python code library that utilizes the OpenAI GPT-3.5 Turbo model to automatically generate README files for code repositories or files. It aims to provide concise summaries of code modules and files, making it easier for developers and users to understand and navigate the codebase.

## Get Started

To install the `gpt_readme` module, follow these steps:

1. Clone the code repository:

```
git clone https://github.com/<username>/gpt_readme.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up your OpenAI API key by exporting it as an environment variable:

```
export OPENAI_API_KEY=<your_api_key>
```

4. Run the module as a script:

```
python -m gpt_readme
```

## Features

The `gpt_readme` module includes the following files and submodules:

- `gpt_readme/__init__.py`: Defines version, author, and URL variables for the module.
- `gpt_readme/__main__.py`: Serves as the entry point for the module and executes the `main` function when run as a script.
- `gpt_readme/constants.py`: Defines constants and variables used in the module, including environment variables, a console object, and dictionaries for file extensions and programming languages.
- `gpt_readme/dir_summary.py`: Provides functionality for summarizing the content of a directory. It recursively traverses the directory structure, generates summaries for files and subdirectories, and utilizes the GPT-3.5 Turbo model to generate a summary of the directory's content.
- `gpt_readme/file_summary.py`: Generates a summary of a given file using the GPT-3.5 Turbo model. It retrieves the file content, determines the language, and constructs a prompt for the model to generate the summary.
- `gpt_readme/main.py`: Orchestrates the generation of the README file. It parses user inputs, scans code extensions, generates code summaries using the GPT-3.5 Turbo model, and saves the README file.
- `gpt_readme/prompts.py`: Defines prompts for generating documentation summaries for code elements such as modules and files. It provides templates for generating prompts for the entire codebase, modules, and files.
- `gpt_readme/utils.py`: Provides utility functions for the project, including handling file operations, generating prompts, and constructing summary pairs.

Please note that if the code modules and files in the `gpt_readme` module do not have sufficient comments or documentation, the generated README content for those components may be limited.

## Acknowledgement

The `gpt_readme` module utilizes the following third-party code libraries:

- OpenAI GPT-3.5 Turbo: A language model developed by OpenAI that generates human-like text based on prompts.

We would like to express our gratitude to OpenAI for providing this powerful language model, which enables us to automate the process of generating informative README files for code repositories and files.
