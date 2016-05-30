# Formatizer
*Literal string formatting for Python versions older than 3.6*

![Formatizer Logo](https://raw.githubusercontent.com/fgimian/formatizer/master/images/formatizer-logo.png)

Awesome artwork provided courtesy of
[Open Clip Art Library](https://openclipart.org/detail/75799/registry-book)

Formatizer is covered by unit tests and Flake8 compliance.  Please note that
this library does use `eval` to perform its expression processing.

## Quick Start

Install Painter in your virtualenv as follows:

```bash
pip install git+https://github.com/fgimian/formatizer.git
```

And now, go ahead and use the f function similarly to [PEP 498](https://www.python.org/dev/peps/pep-0498/):

e.g.

```python
from __future__ import print_function
from formatizer import f

GREETING = 'hi'

def main():
    name = 'Fotis'
    print(f('My name is {name}, I say {GREETING} and 1 + 2 is {1 + 2}'))

if __name__ == '__main__':
    main()
```

All local and global variables will be recognised by the `f` function and
complete Python expressions are also allowed between the braces much like
Python 3.6.
