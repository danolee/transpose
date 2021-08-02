transpose
===========

Command line app that will read in contents of a specified file and output the largest word and transpose/reverse that word.

Example file
```
a
ab
abc
abcd
abcde
```
 
Example output
```
abcde
edcba
```

## Assumptions

- From `man wc`: A word is a non-zero-length sequence of characters delimited by white space
    - Allows for multiple words per line in file
- File must be readable and not empty
- By default, if ties for largest word exist, then the first occurence will be returned; `-a` flag can be passed to return all occurences

## Setup

    $ git clone <repo url>
    $ cd transpose
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install .

## Run tests

    $ pytest

Additionally, to generate an html coverage report (which can be viewed under `htmlcov/index.html`):

    $ pytest --cov=transpose --cov-report=html

## Run app

Default case to read file and output the largest word and the transpose of the largest word; first occurence if ties exists:

    $ ./transpose.py </path/to/file.txt>

If multiple words tie for the largest word, an option to output all of largest words and the transpose of the largest words as lists:

    $ ./transpose.py </path/to/file.txt> -a

## Meta

Daniel Lee – [danolee](https://github.com/danolee)

https://github.com/danolee/transpose