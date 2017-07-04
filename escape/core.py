"""
This module provides a simple class to manage styling strings in the terminal
"""

from .ansi_styles import (
    ColorMixin,
    BackGroundColorMixin,
    ModifiersMixin
)


class Escape(ColorMixin, BackGroundColorMixin, ModifiersMixin, object):
    """
    Simple string like class to produce ansi-escaped strings
    """

    def __init__(self, *args):
        self._original_string = ''.join([str(arg) for arg in args])
        self._styled_string = self._original_string

    def __eq__(self, other):
        return other == self._styled_string

    def __str__(self):
        return self._styled_string

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self._styled_string + str(other)

    def __radd__(self, other):
        return str(other) + self._styled_string

    def __len__(self):
        return len(self._original_string)

    def __mul__(self, other):
        return self._styled_string * other
