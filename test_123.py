import pytest
from rep import compare_numbers

def test_equal_numbers():
    assert compare_numbers(123, 123) == "Yes"

def test_different_numbers():
    assert compare_numbers(123, 456) == "No"

def test_equal_first_digits():
    assert compare_numbers(123, 198) == "No"

def test_zero_and_positive():
    assert compare_numbers(0, 0) == "Yes"
    assert compare_numbers(0, 1) == "No"

def test_negative_numbers():
    assert compare_numbers(-123, -123) == "Yes"
    assert compare_numbers(-123, -456) == "No"
    assert compare_numbers(-123, 123) == "No"

def test_invalid_input():
    assert compare_numbers("123", 123) == "No"
    assert compare_numbers(123, "123") == "No"
    

def test_none_input():
    with pytest.raises(ValueError):
        compare_numbers(None, 123)
    with pytest.raises(ValueError):
        compare_numbers(123, None)

def test_invalid_input():
    with pytest.raises(ValueError):
        compare_numbers("123", 123)
    with pytest.raises(ValueError):
        compare_numbers(123, "456")
    with pytest.raises(ValueError):
        compare_numbers("abc", "abc")

def test_empty_first_input():
    with pytest.raises(ValueError):
        compare_numbers("", 123)

def test_empty_second_input():
    with pytest.raises(ValueError):
        compare_numbers(123, "")