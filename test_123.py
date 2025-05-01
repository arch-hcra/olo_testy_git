import pytest

from rep import compare_numbers

def test_equal_numbers():
    assert compare_numbers("123", "123") == "Yes"

def test_different_numbers():
    assert compare_numbers("123", "456") == "No"

def test_equal_first_characters():
    assert compare_numbers("123", "198") == "Yes"

def test_different_types():
    assert compare_numbers("abc", "123") == "No"

def test_empty_first_input():
    with pytest.raises(IndexError):
        compare_numbers("", "123")

def test_empty_second_input():
    with pytest.raises(IndexError):
        compare_numbers("123", "")