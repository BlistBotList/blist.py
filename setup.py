import setuptools

with open("PIP_README.md", encoding="utf-8") as pip_readme:
    description = pip_readme.read()

setuptools.setup(
    name="blistpy",
    version="0.0.2",
    author="Joshua Patel",
    description="Python API wrapper for the Blist Discord bot list",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshuapatel/blist-wrapper",
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
    keywords="discord discordapp bot blist botlist list blistpy",
    install_requires=["aiohttp"],
    python_requires=">=3.5.3"
)