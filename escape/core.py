"""
This module implements the core terminal styling functionality
"""

from .ansi import (
    ColorMixin
)


class Escape(ColorMixin, object):
    """

    """
    def __init__(self, s):
        self._original = s
        self._string = s

    def __eq__(self, other):
        return other == self._string

    def __str__(self):
        return self._string

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self._string + other

    def __radd__(self, other):
        return other + self._string


