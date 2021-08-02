from setuptools import find_packages
from setuptools import setup

setup(
    name = "transpose",
    version = "1.0",
    description = "",
    author = "Daniel Lee",
    packages = find_packages(),
    setup_requires = ["wheel"],
    install_requires = [
        "attrs==21.2.0",
        "coverage==5.5",
        "iniconfig==1.1.1",
        "packaging==21.0",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pycodestyle==2.7.0",
        "pyparsing==2.4.7",
        "pytest==6.2.4",
        "pytest-cov==2.12.1",
        "toml==0.10.2"
    ],
    entry_points = {
        "console_scripts": [
            "transpose = transpose:main"
        ]
    }
)