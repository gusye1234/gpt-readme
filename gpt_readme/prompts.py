# written in chinese
SYSTEM_PROMPT = """
你是一个经验丰富的{language}程序员，你的工作是要解释总结代码'模块'或者'代码文件'.你的总结将被其他程序员和被使用者阅读, 并用你的总结来学习这部分代码'模块'或者'代码文件'. 你需要保持严谨, 诚实, 不能生成不存在或者错误的描述来误导他人.
请注意, 你是一个严谨的代码工程师, 要完成文档撰写的需求. 不要回复除了代码文档总结外其余无关的内容. 你不需要复述代码.

最重要的是, 阅读你的文档的人使用的语言是'{human_language}', 你必须按照'{human_language}'语言生成你的回复! 如果生成的文档不是'{human_language}'语言的话, 会有非常严重的后果
"""

MODULE_PROMPT = """
如下是{language}模块的'子模块'和'代码文件'的Markdown文档, 这个模块相对于整个代码库的代码路径是{path}, 你需要理解, 总结并推理这个模块的功能. 

这个模块包含如下的'代码文件', 每个'代码文件'对应的注释也包含在其中. 文件内容用[]包裹起来, 如果内容为空则说明模块不包含任何文件:
[{file_summaries}]

---
### 这个模块包含如下的'子模块', 每个'子模块'对应的注释也包含在其中. '子模块'内容用[]包裹起来, 如果内容为空则说明模块不包含任何'子模块':
[{module_summaries}]
---
请你用Markdown格式写下这个模块的总结. 根据上述提供的注释, 将这个模块分成如下几个章节进行总结:
Introduction: 你需要在这个章节提供一个简单的介绍, 介绍这个模块的作用, 以及这个模块的主要功能.
Implementation: 你需要在这个章节总结这个模块里不同功能对应的'代码文件'以及'子模块'. 你需要根据'子模块'和'代码文件'的描述, 提供代码所在位置和功能的总结. 如果你发现这个模块并没有注释或者代码输入的话, 则忽视这个章节的总结
Dependency: 你需要在这个章节专业的识别总结这个模块包含的'子模块'和'代码文件'之间存在的依赖关系. 你需要仔细识别和总结'子模块'和'代码文件'之间具体的依赖关系, 展示它们互相依赖组成的功能, 这对你最终的总结很重要. 同时列举出不属于这个模块的第三方依赖有哪些
Command-line Usage: 请你一步步观察发现'子模块'和'代码文件'的描述中是否含有命令行参数指令来指使如何使用这个代码库. 如果有的话, 请你在这个章节的总结中列举出正确的命令行使用方法, 以及正确的命令行参数选项有哪些, 这对你后续的总结很重要. 否则不需要生成这一章节

请你精简你的专业总结
"""

FILE_PROMPT = """
如下是{language}文件的'代码文件', 文件相对于整个代码库的代码路径是{path}, 你需要理解, 总结并推理这个文件的功能. 
'代码文件'包含如下的代码:
```
{code}
```
请你用Markdown格式写下这个'代码文件'的总结. 根据上述提供的注释, 将这个'代码文件'分成如下几个章节进行总结:
Introduction: 你需要在这个章节提供一个简单的介绍, 介绍'代码文件'实现的功能, 在整个代码库中可能存在的作用, 以及他可能被使用的场景
Implementation: 你需要在这个章节总结'代码文件'实现的功能与它的类, 变量, 函数之间的关系. 如果你发现'代码文件'并没有代码输入的话, 则忽视这个章节的总结
Dependency: 你需要在这个章节总结'代码文件'里包含的引用依赖的类, 变量, 函数有哪些, 并且分别推理总结这些依赖的引用名称或者相对路径, 以及依赖对应的功能是什么.
Command-line Usage: 如果你发现'代码文件'含有命令行参数指令. 请你在这个文件的总结中列举出正确的命令行使用方法, 以及正确的命令行参数选项有哪些, 这对你后续的总结很重要. 如果只是包含函数, 类等代码逻辑的话, 这不需要生成这一章节

请你精简你的专业总结, 并尽量控制在{max_length}个字符以内.
"""

FINAL_PROMPT = """
如下是一整个{language}代码库的解释, 这个代码库的代码路径是{path}:
[{module_summaries}]

你需要理解, 总结这个代码库的功能, 并且生成一个容易理解, 专业的README文档. 涉及到文件路径时, 应当当成代码处理
请你用Markdown格式写下这个代码库的README. 根据上述提供的信息, 你需要首先强调出代码库的名字, 然后将这个模块分成如下几个章节进行总结:

Introduction: 你需要在这个章节提供一个简单的介绍, 介绍这个代码库的作用, 以及这个代码库的主要功能.
Get Started: 你需要在这个章节, 根据上述信息提供安装和使用介绍, 正确明朗的告诉用户如何安装这个代码库.然后根据代码库所使用的代码语言和提供的信息, 提供正确的命令行参数来使用这个代码库, 展示正确的代码接口.
Feature: 你需要在这个章节简洁总结这个代码库支持的主要功能, 并且提供主要功能的用户使用场景与使用方式
Implementation: 你需要在这个章节总结这个代码库里不同功能对应的文件以及'子模块'. 你需要根据'子模块'和'代码文件'的描述, 提供代码所在位置和功能的总结. 如果你发现这个模块并没有注释或者代码输入的话, 则忽视这个章节的总结
Acknowledgement: 你需要在这个章节总结这个代码库用到的外部第三方代码库, 并且分别介绍他们的功能. 不需要介绍这个代码库内部的模块和代码. 在这个章节的最后表示你的感谢

此外, 在不改变整体总结架构的情况下, 你需要满足如下的需求:
{user_demand}
"""

# FILE_NEXT_PROMPT = """
# 你现在正在逐步理解总结一个{language}文件的代码, 文件相对于整个代码库的代码路径是{path}. 你需要最终推理这个文件的功能.

# 你之前已经理解总结过的内容有:
# [{before_summary}]
# 你当前正在理解总结的代码:
# ```
# {code}
# ```

# 请你用Markdown格式写下这个文件的总结. 根据上述提供的注释, 将这个文件分成如下几个章节进行总结:
# Introduction: 你需要在这个章节提供一个简单的介绍, 介绍这个文件实现的功能, 以及他可能被使用的场景
# Features: 你需要在这个章节总结这个文件实现的功能与它的类, 变量, 函数之间的关系.

# 请你精简你的专业总结, 并尽量控制在{max_length}个字符以内.
# """
