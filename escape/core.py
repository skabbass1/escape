"""
This module implements the core terminal styling functionality
"""

from .ansi_styles import (
    ColorMixin,
    BackGroundColorMixin,
    ModifiersMixin
)


class Escape(ColorMixin, BackGroundColorMixin, ModifiersMixin, object):
    """

    """

    def __init__(self, *args):
        self._original = ''.join([str(arg) for arg in args])
        self._string = self._original

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
