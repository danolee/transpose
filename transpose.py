#!/usr/bin/env python
"""Transpose largest word(s) in file"""

import argparse
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('transpose.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_file_to_list(filename):
    """
    Loads file contents as a list
    
    :param filename: the name of the file
    :returns: the file contents as a list of strings
    :raises IOError: if filename can not be found or can not be read
    """
    word_data = []
    
    try:
        # read contents of file, then close
        with open(filename) as f:
            # loop through each line and add each word to list
            for line in f:
                for word in line.split():
                    word_data.append(word)
        return word_data
    except IOError as e:
        logger.exception("could not read file")
        return None


def find_largest_words(word_data):
    """
    Returns list of largest strings
    
    :param word_data: list of strings to search for largest word
    :returns: list of strings of only the largest words
    :raises ValueError: if list is empty
    :raises TypeError: if list is not composed of strings
    or if word_data is not a list
    """
    largest_words = []

    try:
        if type(word_data) is not list:
            raise TypeError
        
        # determine length of largest words
        largest_length = max(map(len, word_data))

        # find all largest words in list; allows for multiple matches
        for word in word_data:
            if len(word) == largest_length:
                largest_words.append(word)

        return largest_words
    except ValueError:
        logger.exception("no words found in list")
        return None
    except TypeError:
        logger.exception("incorrect object type")
        return None
   

def transpose_words_in_list(word_data):
    """
    Reverses each string in the list
    
    :param word_data: list of strings to reverse
    :returns: list of strings reversed
    :raises TypeError: if list is not composed of strings
    or if word_data is not a list
    """
    transposed_data = []

    try:
        if type(word_data) is not list:
            raise TypeError
        
        # transpose/reverse all words within list
        for word in word_data:
            if type(word) is not str:
                logger.exception("word in list is not a str")
                raise ValueError
                
            transposed_data.append(word[::-1])
        return transposed_data
    except ValueError:
        logger.exception("no words found in list")
        return None
        
    except TypeError:
        logger.exception("incorrect object type")
        return None
            

def parse_options(argv):
    """
    Parse and return command line args

    :param argv: command line arguments
    :returns: populated namespace
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", help="input file to process")
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="if multiple words tie for largest, \
             print them all instead of the first occurence")
    return parser.parse_args(argv[1:])


def main(argv):
    args = parse_options(argv)

    file_data = load_file_to_list(args.filename)
    largest_words = find_largest_words(file_data)
    transposed_words = transpose_words_in_list(largest_words)
    
    if largest_words is not None and transposed_words is not None:
        if args.all:
            # if --all flag is used, print all occurences as a list
            print(largest_words)
            print(transposed_words)
        else:
            # by default, only print first occurence
            print(largest_words[0])
            print(transposed_words[0])


if __name__ == "__main__":
    main(sys.argv)
