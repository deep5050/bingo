from setuptools import find_packages
from setuptools import setup
from bingo import __app_name__,__version__

DESCRIPTION = "A Bing wallpaper downloader utility"

def required():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="bingo-cli",
    version=__version__,
    description=DESCRIPTION,
    long_description="A Bing wallpaper downloader utility",
    long_description_content_type="text/markdown",
    keywords="Bing wallpaper downloader cli-app",
    author="Dipankar Pal",
    author_email="dipankarpal5050@gmail.com",
    url="https://github.com/deep5050/bingo",
    license="MIT",
    entry_points={
        "console_scripts": [
            "bingo = bingo.__main__:main"
        ]
    },
    packages=find_packages(),
    install_requires=required(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/deep5050/bingo/"
    },
)