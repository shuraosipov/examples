import string
import secrets
import pytest
from myapp.decorators import generate_string


def test_default_length():
    password = generate_string()
    assert len(password) == 8


def test_custom_length():
    password = generate_string(12)
    assert len(password) == 12


def test_contains_letters_and_digits():
    password = generate_string(10)
    assert any(c.isalpha() for c in password)
    assert any(c.isdigit() for c in password)


def test_different_strings():
    password1 = generate_string()
    password2 = generate_string()
    assert password1 != password2
