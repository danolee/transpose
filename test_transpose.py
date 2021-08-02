#!/usr/bin/env python
"""Test coverage for transpose.py"""

import transpose
import pytest


def test_load_valid_file():
    """Tests to verify transpose.load_file_to_list(filename) with valid file"""
    assert transpose.load_file_to_list(
        "test_files/test_data1.txt"
    ) == ["abc", "xyz", "mnop", "qrstu", "jk", "1234-", "102354"]


def test_load_empty_file():
    """Tests to verify transpose.load_file_to_list(filename) with empty file"""
    assert transpose.load_file_to_list("test_files/test_data2.txt") == []


def test_load_invalid_file():
    """Tests to verify transpose.load_file_to_list(filename) with
    invalid file"""
    assert transpose.load_file_to_list("test_files/dne.txt") is None


def test_find_largest_words_one_largest():
    """Tests to verify transpose.find_largest_words(list) when
    only one word is largest"""
    assert transpose.find_largest_words(["abc", "abcde", "ab"]) == ["abcde"]
    

def test_find_largest_words_multiple_largest():
    """Tests to verify transpose.find_largest_words(list) when multiple
    words tie for the largest"""
    assert transpose.find_largest_words(
        ["abc", "abcde", "12345"]
    ) == ["abcde", "12345"]


def test_find_largest_words_empty_list():
    """Tests to verify transpose.find_largest_words(list) when list is empty"""
    assert transpose.find_largest_words([]) is None


def test_find_largest_words_no_string():
    """Tests to verify transpose.find_largest_words(list) when list does not
    have a string"""
    assert transpose.find_largest_words(["abc", "abcde", 12345]) is None
    

def test_find_largest_words_int_only():
    """Tests to verify transpose.find_largest_words(list) when list has
    an int"""
    assert transpose.find_largest_words(123) is None
    

def test_find_largest_words_string_only():
    """Tests to verify transpose.find_largest_words(list) when sent a string"""
    assert transpose.find_largest_words("testing") is None
    

def test_transpose_words_in_list_one_word():
    """Tests to verify transpose.transpose_words_in_list(list) when there's
    only one word in list"""
    assert transpose.transpose_words_in_list(["abcde"]) == ["edcba"]
    

def test_transpose_words_in_list_multiple_words():
    """Tests to verify transpose.transpose_words_in_list(list) when there are
    multiple words in list"""
    assert transpose.transpose_words_in_list(
        ["abc", "12345"]
    ) == ["cba", "54321"]
    

def test_transpose_words_in_list_empty_list():
    """Tests to verify transpose.transpose_words_in_list(list) when list
    is empty"""
    assert transpose.transpose_words_in_list([]) == []
    

def test_transpose_words_in_list_not_string():
    """Tests to verify transpose.transpose_words_in_list(list) when list
    does not contain a string"""
    assert transpose.transpose_words_in_list(["abc", "abcde", 12345]) is None


def test_transpose_words_in_list_int_only():
    """Tests to verify transpose.transpose_words_in_list(list) when sent
    an int"""
    assert transpose.transpose_words_in_list(123) is None


def test_transpose_words_in_list_string_only():
    """Tests to verify transpose.transpose_words_in_list(list) when sent
    a string"""
    assert transpose.transpose_words_in_list("testing") is None


# parametrizing command line and expected outputs for test function
@pytest.mark.parametrize(
    "cmd_arg, exp_largest, exp_transpose",
    [
        pytest.param(
            ["transpose.py", "test_files/test_data1.txt"],
            "102354",
            "453201",
            id="file_single_first"
        ),
        pytest.param(
            ["transpose.py", "test_files/test_data1.txt", "-a"],
            "['102354']",
            "['453201']",
            id="file_single_all"
        ),
        pytest.param(
            ["transpose.py", "test_files/test_data3.txt"],
            "qrstuv",
            "vutsrq",
            id="file_multi_first"),
        pytest.param(
            ["transpose.py", "test_files/test_data3.txt", "-a"],
            "['qrstuv', '102354']",
            "['vutsrq', '453201']",
            id="file_multi_all"
        ),
        pytest.param(
            ["transpose.py", "test_files/test_data4.txt"],
            "one_word",
            "drow_eno",
            id="file_one_word"),
        
    ],
)
def test_transpose_main_parametrize(
    capsys,
    cmd_arg,
    exp_largest,
    exp_transpose
):
    """Tests to verify transpose.main(list) with pytest parameterization"""
    transpose.main(cmd_arg)

    # capture stdout for comparison
    captured = capsys.readouterr()
    captured_split = captured.out.split("\n")
    assert captured_split[0] == exp_largest
    assert captured_split[1] == exp_transpose


def test_transpose_main_file_not_found():
    """Tests to verify transpose.main(list) when file can not be found"""
    assert transpose.main(
        [
            "transpose.py",
            "test_files/test_data2.txt"
        ]
    ) is None


def test_transpose_main_file_empty():
    """Tests to verify transpose.main(list) when file is empty"""
    assert transpose.main(["transpose.py", "test_files/dne.txt"]) is None
