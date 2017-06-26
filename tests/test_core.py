"""
Unittests for the core module
"""
from escape.core import Escape


def test_string_gets_styled():
    assert Escape('Hello World').red() == u'\u001b[31mHello World\u001b[39m'
    # assert Escape('Hello World').blue() == u'\u001b[31mHello World\u001b[39m'
    # assert Escape('Hello World').underline() == u'\u001b[31mHello World\u001b[39m'
    # assert Escape('Hello World').bold() == u'\u001b[31mHello World\u001b[39m'


def test_multiple_styles_get_applied():
    pass

