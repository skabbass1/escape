# -*- coding: utf-8 -*-
"""
This module provides a simple class to manage styling strings in the terminal
"""

import sys
import itertools

from .ansi_styles import (
    ColorMixin,
    BackGroundColorMixin,
    ModifiersMixin
)

PY3 = sys.version_info[0] >= 3


class Escape(ColorMixin, BackGroundColorMixin, ModifiersMixin, object):
    """
    Simple string like class to produce ansi-escaped strings
    """

    def __init__(self, *args):

        self._original_string = ''.join(
            [arg.encode('utf-8') if (not PY3 and isinstance(arg, unicode)) else str(arg) for arg in args]
        )
        self._styled_string = self._original_string

    def __unicode__(self):
        styled_string = self._styled_string
        if isinstance(styled_string, bytes):
            return styled_string.decode('utf8')
        return styled_string

    if PY3:
        __str__ = __unicode__
    else:
        def __str__(self):
            return self._styled_string

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return other == self._styled_string

    def __add__(self, other):
        return self._styled_string + other

    def __radd__(self, other):
        return other + self._styled_string

    def __len__(self):
        return len(self._original_string)

    def __mul__(self, other):
        return self._styled_string * other


def palette():
    colors = [a for a in dir(ColorMixin) if not a.startswith('_')]
    bg_colors = [a for a in dir(BackGroundColorMixin) if not a.startswith('_')]
    modifiers = [a for a in dir(ModifiersMixin) if not a.startswith('_')]
    max_attribute_name_len = len(max(colors + bg_colors + modifiers, key=len))
    string = 'Hello World'
    table_width = max_attribute_name_len + len(string) + 3
    for c in itertools.chain(colors, bg_colors, modifiers):
        print('-' * table_width)
        print(c.ljust(max_attribute_name_len) + '|', getattr(Escape(string), c)() + '|')
    print('-' * table_width)

