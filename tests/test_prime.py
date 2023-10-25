# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors


def test_not_integer():
    """
    Write a test that asserts that when generate_prime_factors is called 
    with a data type that is not an integer 
    (e.g. a string or float), a ValueError is raised. 
    Write the appropriate code to solve this and then commit the changes.
    """
    with pytest.raises(ValueError, match="Enter only integers"):
        list(generate_prime_factors("l"))
    with pytest.raises(ValueError, match="Enter only integers"):
        list(generate_prime_factors(1.5))

def test_1_emptylist():
    """
    Write a test that asserts that when generate_prime_factors is called with 1, 
    an empty list is returned. Solve & commit.
    """
    assert not list(generate_prime_factors(1))

def test_2is_2():
    """
    Write a test that asserts that when generate_prime_factors is called with 2, 
    the list [2] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(2)) == [2]

def test_3is_3():
    """
    Write a test that asserts that when generate_prime_factors is called with 3, 
    the list [3] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(3)) == [3]

def test_4():
    """
    Write a test that asserts that when generate_prime_factors is called with 4, 
    the list [2, 2] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(4)) == [2,2]

def test_6():
    """
    Write a test that asserts that when generate_prime_factors is called with 6,
    the list [2, 3] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(6)) == [2,3]

def test_8():
    """
    Write a test that asserts that when generate_prime_factors is called with 8, 
    the list [2, 2, 2] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(8)) == [2,2,2]

def test_9():
    """
    Write a test that asserts that when generate_prime_factors is called with 9, 
    the list [3, 3] is returned. Solve & commit.
    """
    assert list(generate_prime_factors(9)) == [3,3]
