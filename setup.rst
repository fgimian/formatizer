.. image:: https://raw.githubusercontent.com/fgimian/formatizer/master/images/formatizer-logo.png
    :alt: Formatizer Logo

Introduction
------------

Formatizer provides literal string formatting for Python versions older than
3.6.  This replaces the need for substitution using % or the format function.

ormatizer is covered by unit tests and Flake8 compliance.  Please note that
this library does use `eval` to perform its expression processing.

Quick Start
-----------

Install Formatizer in your virtualenv as follows:

.. code:: bash

    pip install formatizer

And now, go ahead and use the f function similarly to
`PEP 498 <https://www.python.org/dev/peps/pep-0498/>`_:

.. code:: python

    from __future__ import print_function
    from formatizer import f

    GREETING = 'hi'

    def main():
        name = 'Fotis'
        print(f('My name is {name}, I say {GREETING} and 1 + 2 is {1 + 2}'))

    if __name__ == '__main__':
        main()

All local and global variables will be recognised by the `f` function and
complete Python expressions are also allowed between the braces much like
Python 3.6.
