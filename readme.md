
<div align="center">
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/written_in-GPT-green">
    </a>
    <a href="https://github.com/gusye1234/gpt-readme">
      <img src="https://img.shields.io/badge/could_be-Wrong-red">
    </a>
</div>
# gpt-readme

## Introduction
The `gpt-readme` module is designed to generate README files for code repositories. It utilizes the OpenAI GPT-3.5 Turbo model to generate summaries for individual files and directories. The generated README includes code summaries and is saved at the specified location.

## Get Started
To install the `gpt-readme` module, follow these steps:

1. Open a terminal.
2. Run the following command to install the package:
   ```
   pip install gpt-readme
   ```

## Features
The `gpt-readme` module consists of the following files and sub-modules:

- `setup.py`: This file configures the installation and distribution of the `gpt-readme` package by extracting metadata from `readme.md` and `gpt_readme/__init__.py` files. It sets up the package details and dependencies.

- `gpt_readme` sub-module: This sub-module includes the following files:
  - `dir_summary.py`: Generates summaries for directories and their contents.
  - `file_summary.py`: Generates a summary for an individual file.
  - `main.py`: Parses command line arguments, uses the GPT-3.5 Turbo model to generate code summaries, and saves the README file.
  - `constants.py`: Defines constants and variables used in the codebase.
  - `prompts.py`: Contains predefined prompts for generating documentation summaries.
  - `utils.py`: Provides utility functions for file processing and generating prompts.
  The `gpt_readme` sub-module also includes `__init__.py` and `__main__.py` files as entry points.

- `gpt_readme.egg-info` sub-module: This sub-module contains metadata and configuration information related to the GPT model.

Please note that if there are no comments or documentation in the code, the corresponding functionality may not be summarized in this section.

## Acknowledgement
The `gpt-readme` module utilizes the following third-party code libraries:

- OpenAI GPT-3.5 Turbo model: This model is used for generating code summaries and README files.

Special thanks to the developers of the OpenAI GPT-3.5 Turbo model for their contribution.