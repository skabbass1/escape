"""
Ansi Color, BackGround Color and Modifier Mixins
"""


class ColorMixin(object):
    """
    A simple mixin class which wraps  input text between
    ansi color escape codes
    """

    _template = u'\u001b[{start}m{text}\u001b[{end}m'

    def black(self):
        pass

    def red(self):
        self._string = self._template.format(start=31, end=39, text=self._string)

        return self

    def green(self):
        self._string = u'{start}{text}{end}'
        return self

    def yellow(self):
        self._string = u'{start}{text}{end}'
        return self
