import setuptools

with open("PIP_README.md", encoding="utf-8") as pip_readme:
    description = pip_readme.read()

setuptools.setup(
    name="blistpy",
    version="0.1.3",
    author="A Discord User & A Trash Coder",
    description="Python API wrapper for the Blist Discord bot list",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlistBotList/blist.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    project_urls = {
        "Source": "https://github.com/BlistBotList/blist.py",
        "Documentation": "https://github.com/BlistBotList/blist.py/blob/master/README.md",
        "Issue tracker": "https://github.com/BlistBotList/blist.py/issues",
    },
    keywords="discord discordapp bot blist botlist list blistpy",
    install_requires=["aiohttp", "python-dateutil"],
    python_requires=">=3.8"
)