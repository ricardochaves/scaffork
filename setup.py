import os

from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="scaffork",
    version="0.0.2",
    description="A simple way to create your project",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    author="Ricardo Baltazar Chaves",
    author_email="ricardobchaves6@gmail.com",
    license="MIT",
    url="https://github.com/scaffork/scaffork",
    packages=find_packages(),
    install_requires=[
        "PyInquirer>=1.0.3",
        "prompt_toolkit==1.0.14",
        "travispy>=0.3.5",
        "gitpython>=2.1.11",
        "pyyaml>=3.13",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Natural Language :: Portuguese (Brazilian)",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # py_modules=["scaffork"],
    entry_points={"console_scripts": ["scaffork=start:patched_main"]},
)
