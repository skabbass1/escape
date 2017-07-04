# -*- coding: utf-8 -*-
"""
Ansi Color, BackGround Color and Modifier Mixins
"""

_STYLE_TEMPLATE = '\x1b[{start}m{text}\x1b[{end}m'


class ColorMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi color escape codes
    """

    def black(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=30, end=39, text=self._styled_string)
        return self

    def red(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=31, end=39, text=self._styled_string)
        return self

    def bright_red(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=91, end=39, text=self._styled_string)
        return self

    def green(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=32, end=39, text=self._styled_string)
        return self

    def bright_green(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=92, end=39, text=self._styled_string)
        return self

    def yellow(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=33, end=39, text=self._styled_string)
        return self

    def bright_yellow(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=93, end=39, text=self._styled_string)
        return self

    def blue(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=34, end=39, text=self._styled_string)
        return self

    def bright_blue(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=94, end=39, text=self._styled_string)
        return self

    def magenta(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=35, end=39, text=self._styled_string)
        return self

    def bright_magenta(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=95, end=39, text=self._styled_string)
        return self

    def cyan(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=36, end=39, text=self._styled_string)
        return self

    def bright_cyan(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=96, end=39, text=self._styled_string)
        return self

    def white(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=37, end=39, text=self._styled_string)
        return self

    def bright_white(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=97, end=39, text=self._styled_string)
        return self

    def gray(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=90, end=39, text=self._styled_string)
        return self


class BackGroundColorMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi background color escape codes
    """

    def black_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=40, end=49, text=self._styled_string)
        return self

    def bright_black_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=100, end=49, text=self._styled_string)
        return self

    def red_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=41, end=49, text=self._styled_string)
        return self

    def bright_red_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=101, end=49, text=self._styled_string)
        return self

    def green_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=42, end=49, text=self._styled_string)
        return self

    def bright_green_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=102, end=49, text=self._styled_string)
        return self

    def yellow_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=43, end=49, text=self._styled_string)
        return self

    def bright_yellow_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=103, end=49, text=self._styled_string)
        return self

    def blue_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=44, end=49, text=self._styled_string)
        return self

    def bright_blue_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=104, end=49, text=self._styled_string)
        return self

    def magenta_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=45, end=49, text=self._styled_string)
        return self

    def bright_magenta_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=105, end=49, text=self._styled_string)
        return self

    def cyan_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=46, end=49, text=self._styled_string)
        return self

    def bright_cyan_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=106, end=49, text=self._styled_string)
        return self

    def white_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=47, end=49, text=self._styled_string)
        return self

    def bright_white_background(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=107, end=49, text=self._styled_string)
        return self


class ModifiersMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi text modifier  escape codes
    """

    def bold(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=1, end=22, text=self._styled_string)
        return self

    def dim(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=2, end=22, text=self._styled_string)
        return self

    def italic(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=3, end=23, text=self._styled_string)
        return self

    def inverse(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=7, end=27, text=self._styled_string)
        return self

    def hidden(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=8, end=28, text=self._styled_string)
        return self

    def strikethrough(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=9, end=29, text=self._styled_string)
        return self

    def underline(self):
        self._styled_string = _STYLE_TEMPLATE.format(start=4, end=24, text=self._styled_string)
        return self
