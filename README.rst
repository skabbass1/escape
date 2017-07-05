|Build Status|

escape
======

Escape is a very simple terminal styling library largely inspired by the
excellent javascript `chalk <https://github.com/chalk/chalk>`__ library.
There are other terminal styling libraries such as
`colorama <https://github.com/tartley/colorama>`__ available but they do
not offer a simple composable API like escape does. Escape is pure
python, does not have any external dependencies and should work right
out of the box. Escape has been tested to work with **python 2.7** and
**python 3.6**. Escape **has not** been tested on Windows

Install
=======

pip install escape

Usage
=====

.. code:: python

    from escape import Escape

    print(Escape('Hello World').red())

    # combine styled strings
    print(Escape('Hello').bright_green() + Escape(' World!').bright_red())

    # combibe styled and normal string
    print(Escape('Hello').bright_magenta() + ' World!')

    # compose multiple styles together
    print(Escape('Hello World').bright_red().underline().bright_yellow_background())

    # Nest styles
    Escape('Hello ', Escape('World').bright_green_background()).bright_red()

    Escape('Hello ' +  Escape('World').bright_green_background()).bright_red()

Preview how styling looks on your terminal
==========================================

.. code:: python

    from escape import palette
    palette()

.. figure:: media/palette.png
   :alt: alt tag

   alt tag

Styles
======

Modifiers
~~~~~~~~~

-  bold
-  dim
-  hidden
-  inverse
-  italic
-  strikethrough
-  underline

Colors
~~~~~~

-  black
-  red
-  green
-  yellow
-  blue
-  magenta
-  cyan
-  white
-  gray
-  bright\_red
-  bright\_green
-  bright\_yellow
-  bright\_blue
-  bright\_magenta
-  bright\_cyan
-  bright\_white

Background Colors
~~~~~~~~~~~~~~~~~

-  black\_background
-  red\_background
-  green\_background
-  yellow\_background
-  blue\_background
-  magenta\_background
-  cyan\_background
-  white\_background
-  bright\_black\_background
-  bright\_red\_background
-  bright\_green\_background
-  bright\_yellow\_background
-  bright\_blue\_background
-  bright\_magenta\_background
-  bright\_cyan\_background
-  bright\_white\_background

.. |Build Status| image:: https://travis-ci.org/skabbass1/escape.svg?branch=master
   :target: https://travis-ci.org/skabbass1/escape
