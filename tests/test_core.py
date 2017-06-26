"""
Unittests for the core module
"""
from escape.core import Escape


def test_string_gets_styled_black():
    assert Escape('hello').black() == u'\x1b[30mhello\x1b[39m'


def test_string_gets_styled_red():
    assert Escape('hello').red() == u'\x1b[31mhello\x1b[39m'


def test_string_gets_styled_bright_red():
    assert Escape('hello').bright_red() == u'\x1b[91mhello\x1b[39m'


def test_string_gets_styled_green():
    assert Escape('hello').green() == u'\x1b[32mhello\x1b[39m'


def test_string_gets_styled_bright_green():
    assert Escape('hello').bright_green() == u'\x1b[92mhello\x1b[39m'


def test_string_gets_styled_yellow():
    assert Escape('hello').green() == u'\x1b[33mhello\x1b[39m'


def test_string_gets_styled_bright_yellow():
    assert Escape('hello').bright_green() == u'\x1b[93mhello\x1b[39m'


def test_string_gets_styled_blue():
    assert Escape('hello').blue() == u'\x1b[34mhello\x1b[39m'


def test_string_gets_styled_bright_blue():
    assert Escape('hello').bright_blue() == u'\x1b[94mhello\x1b[39m'


def test_string_gets_styled_magenta():
    assert Escape('hello').magenta() == u'\x1b[35mhello\x1b[39m'


def test_string_gets_styled_bright_magenta():
    assert Escape('hello').bright_magenta() == u'\x1b[95mhello\x1b[39m'


def test_string_gets_styled_cyan():
    assert Escape('hello').cyan() == u'\x1b[36mhello\x1b[39m'


def test_string_gets_styled_bright_cyan():
    assert Escape('hello').bright_magenta() == u'\x1b[96mhello\x1b[39m'


def test_string_gets_styled_white():
    assert Escape('hello').white() == u'\x1b[37mhello\x1b[39m'


def test_string_gets_styled_bright_white():
    assert Escape('hello').bright_white() == u'\x1b[97mhello\x1b[39m'


def test_string_gets_styled_gray():
    assert Escape('hello').gray() == u'\x1b[90mhello\x1b[39m'


def test_multiple_styles_get_applied():
    assert Escape('Hello World').red().blue() == u'\x1b[34m\x1b[31mHello World\x1b[39m\x1b[39m'


def test_conatenate_with_other_strings():
    assert Escape('hello') + ' world' == 'hello world'
    assert 'world,' + Escape('Hi!').green() == u'world,\x1b[32mHi!\x1b[39m'
