import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()


vars2find = ['__author__', '__version__', '__url__']
vars2readme = {}
with open("./gpt_readme/__init__.py") as f:
    for line in f.readlines():
        for v in vars2find:
            if line.startswith(v):
                line = line.replace(" ", '').replace("\"", '').replace("\'", '').strip()
                vars2readme[v] = line.split('=')[1]

setuptools.setup(
    name='gpt_readme',
    url=vars2readme['__url__'],
    version=vars2readme['__version__'],
    author=vars2readme['__author__'],
    description='Use ChatGPT to generate a well-formatted README based on your code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['gpt_readme'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=['openai', 'rich'],
    entry_points={
        'console_scripts': [
            'gpt_readme = gpt_readme:main',
        ]
    },
)
