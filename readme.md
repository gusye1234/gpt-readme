
<div align="center">
   <div>
     <a href="https://github.com/gusye1234/gpt-readme/blob/main/readme_human.md">
      Check out the human-written readme here
    </a>
    <br/>
    <br/>
  </div>
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

*This readme generated by command: `gpt_readme --path="./gpt_readme" --demand="Add detailed commandline usage of gpt_readme, also inform user about how to config OpenAI API key. Let user know they can install gpt_readme from pip, or from source github repo gusye1234/gpt-readme" --language="english"`*

# gpt_readme

A Python module for generating README documentation for code repositories or files using the OpenAI GPT-3.5 Turbo model.

## Introduction

The `gpt_readme` module provides functionality for generating README documentation for code repositories or files. It utilizes the OpenAI GPT-3.5 Turbo model to generate summaries based on prompts constructed from the code and file information. This module serves as an entry point for generating README files and includes various utility functions and constant variables.

## Get Started

### Installation

You can install `gpt_readme` using pip:

```
pip install gpt_readme
```

Alternatively, you can clone the source code from the GitHub repository [gusye1234/gpt-readme](https://github.com/gusye1234/gpt-readme) and install it manually.

### Command-line Usage

To use this module, run the following command:

```
gpt_readme --path=<path> --exts=<extensions> --language=<language> --demand=<demand> --out=<output_file>
```

- `--path`: Specify the local path for the code repository or file.
- `--exts`: Select the code extension names, separated by commas.
- `--language`: Select the language for the README.
- `--demand`: Additional requirements for the generated README.
- `--out`: Specify the location to save the README file.

Note: Before using `gpt_readme`, make sure to configure your OpenAI API key using the appropriate method recommended by OpenAI.

## Features

- `dir_summary.py`: Contains functions for summarizing the content of a directory, generating summaries for each file and module.
- `file_summary.py`: Provides functionality for generating a summary of a given file using the OpenAI GPT-3.5 Turbo model.
- `main.py`: The main file that executes the code, allowing users to specify the path, code extensions, language, and additional requirements for the generated README.
- `prompts.py`: Contains prompts and templates for generating README documentation for code modules or files.
- `utils.py`: Provides various utility functions for working with files and generating prompts and summaries.

## Acknowledgment

This module is powered by the following third-party libraries:

- [OpenAI GPT-3.5 Turbo](https://openai.com): The language model used for generating the README documentation.

Special thanks to the developers of these libraries for their valuable contributions.

## Conclusion

The `gpt_readme` module is a powerful tool for automatically generating README documentation for code repositories or files. It leverages the OpenAI GPT-3.5 Turbo model to provide accurate and informative summaries. With its easy-to-use command-line interface and various features, `gpt_readme` simplifies the process of creating README files, saving developers time and effort.
