"""Tests for the calculator module."""

import pytest
from calculator import calculate


def test_addition():
    assert calculate(2, "+", 3) == 5


def test_subtraction():
    assert calculate(10, "-", 4) == 6


def test_multiplication():
    assert calculate(3, "*", 7) == 21


def test_division():
    assert calculate(20, "/", 4) == 5.0


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, "/", 0)


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(1, "%", 2)


def test_negative_numbers():
    assert calculate(-5, "+", 3) == -2


def test_float_numbers():
    assert calculate(1.5, "*", 2) == 3.0


def test_subtraction_negative_result():
    assert calculate(3, "-", 10) == -7
