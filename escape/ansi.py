"""
Ansi Color, BackGround Color and Modifier Mixins
"""


class ColorMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi color escape codes
    """

    _template = u'\x1b[{start}m{text}\x1b[{end}m'

    def black(self):
        self._string = self._template.format(start=30, end=39, text=self._string)
        return self


    def red(self):
        self._string = self._template.format(start=31, end=39, text=self._string)
        return self

    def bright_red(self):
        self._string = self._template.format(start=91, end=39, text=self._string)
        return self

    def green(self):
        self._string = self._template.format(start=32, end=39, text=self._string)
        return self

    def bright_green(self):
        self._string = self._template.format(start=92, end=39, text=self._string)
        return self

    def yellow(self):
        self._string = self._template.format(start=33, end=39, text=self._string)
        return self

    def yellow_bright(self):
        self._string = self._template.format(start=93, end=39, text=self._string)
        return self

    def blue(self):
        self._string = self._template.format(start=34, end=39, text=self._string)
        return self

    def bright_blue(self):
        self._string = self._template.format(start=94, end=39, text=self._string)
        return self

    def magenta(self):
        self._string = self._template.format(start=35, end=39, text=self._string)
        return self

    def bright_magenta(self):
        self._string = self._template.format(start=95, end=39, text=self._string)
        return self

    def cyan(self):
        self._string = self._template.format(start=36, end=39, text=self._string)
        return self

    def bright_cyan(self):
        self._string = self._template.format(start=96, end=39, text=self._string)
        return self

    def white(self):
        self._string = self._template.format(start=37, end=39, text=self._string)
        return self


    def bright_white(self):
        self._string = self._template.format(start=97, end=39, text=self._string)
        return self

    def gray(self):
        self._string = self._template.format(start=90, end=39, text=self._string)
        return self


class BackGroundColorMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi background color escape codes
    """

    _template = u'\u001b[{start}m{text}\u001b[{end}m'


