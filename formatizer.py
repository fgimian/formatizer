from __future__ import print_function


import inspect
import sys


PY3 = sys.version_info[0] == 3
if PY3:  # pragma: no cover
    import _string


class LiteralFormatter(object):
    def format(self, format_string, globals_, locals_, recursion_depth=2):
        if recursion_depth < 0:
            raise ValueError('Max string recursion exceeded')

        # Parse the format string and build the result
        result = []

        for literal_text, expression, format_spec, conversion in \
                self.parse(format_string):

            # Regular text (e.g. 'Hello there')
            if literal_text:
                result.append(literal_text)

            # An expression (e.g. '{1 + 2}')
            if expression is not None:
                obj = eval(expression, globals_, locals_)
                obj = self.convert_field(obj, conversion)
                format_spec = self.format(format_spec, globals_, locals_,
                                          recursion_depth - 1)
                result.append(format(obj, format_spec))

        return ''.join(result)

    def parse(self, format_string):
        if PY3:
            return _string.formatter_parser(format_string)  # pragma: no cover
        else:
            return format_string._formatter_parser()  # pragma: no cover

    def convert_field(self, value, conversion):
        if conversion is None:
            return value
        elif conversion == 's':
            return str(value)
        elif conversion == 'r':
            return repr(value)
        raise ValueError(
            "Unknown conversion specifier {0!s}".format(conversion)
        )


def f(format_string, back=1):
    caller_frame = inspect.currentframe()
    for _ in range(back):
        caller_frame = caller_frame.f_back
    caller_globals = caller_frame.f_globals
    caller_locals = caller_frame.f_locals
    lf = LiteralFormatter()
    return lf.format(format_string, caller_globals, caller_locals)


def fprint(*args, **kwargs):
    args = tuple(str(f(_, back=3)) for _ in args)
    print(*args, **kwargs)
