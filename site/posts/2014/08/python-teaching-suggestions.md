.. title: Some Suggestions for Teaching Python
.. slug: python-teaching-suggestions
.. date: 2014-08-08 12:55:26 UTC
.. tags: python
.. link: 
.. description: 
.. type: text

I recently had the chance to attend a Software Carpentry bootcamp at the
University of Queensland (as a teaching assistant), as well as seeing a
presentation from one of UQ's tutors at PyCon Australia 2014.

While many of the issues they encountered were inherent in the complexity
of teaching programming, a few seemed like things that could be avoided.

# Getting floating point results from integer division

In Python 2, integer division copies C in truncating the answer by default:

```sh
    $ python -c "print(3/4)"
    0
```

Promoting to floating point requires type coercion, a command line flag
or a future import:

```sh
    $ python -c "print(float(3)/4)"
    0.75
    $ python -Qnew -c "print(3/4)"
    0.75
    $ python -c "from __future__ import division; print(3/4)"
    0.75
```

Python 3 just does the right thing by default, so one way to avoid the
problem entirely is to teach Python 3 instead of Python 2:

```sh
    $ python3 -c "print(3/4)"
    0.75
```

(In both Python 2 and 3, the `//` floor division operator explicitly
requests truncating division when it is desired)

# Common Python 2/3 syntax for printing values

I've been using Python 2 and 3 in parallel for more than 8 years now (while
Python 3.0 was released in 2008, the project started in earnest a couple
of years earlier than that, while Python 2.5 was still in development).

One essential trick I have learned in order to make regularly switching back
and forth feasible is to limit myself to the common print syntax that works
the same in both versions: passing a single argument surrounded by
parentheses.

```sh
$ python -c 'print("Hello world!")'
Hello world!
$ python3 -c 'print("Hello world!")'
Hello world!
```

If I need to pass multiple arguments, I'll use string formatting, rather
than the implicit concatenation feature.

```sh
$ python -c 'print("{} {}{}".format("Hello", "world", "!"))'
Hello world!
$ python3 -c 'print("{} {}{}".format("Hello", "world", "!"))'
Hello world!
```

Rather than doing this, the Software Carpentry material that was used at the
bootcamp I attended used the legacy Python 2 only `print` syntax extensively,
causing examples that otherwise would have worked fine in either version to
fail for students that happened to be running Python 3. Adopting the shared
syntax for printing values could be enough to make the course largely
version independent.

# Distinguishing between returning and printing values

One problem noted both at the bootcamp and by presenters at PyCon Australia
was the challenge of teaching students the difference between printing and
returning values. The problem is the "Print" part of the Read-Eval-Print-Loop
provided by Python's interactive interpreter:

```python
>>> def print_arg(x):
...     print(x)
...
>>> def return_arg(x):
...     return x
...
>>> print_arg(10)
10
>>> return_arg(10)
10
```

There's no obvious difference in output at the interactive prompt, especially
for types like numbers where the results of `str` and `repr` are the same.
Even when they're different, those differences may not be obvious to a
student:

```python
>>> print_arg("Hello world")
Hello world
>>> return_arg("Hello world")
'Hello world'
```

While I don't have a definitive answer for this one, an experiment that seems
worth trying to me is to teach students how to replace `sys.displayhook`. In
particular, I suggest demonstrating the following change, and seeing if it
helps explain the difference between printing output for display to the user
and returning values for further processing:

```python
>>> def new_displayhook(obj):
...     if obj is not None:
...         print("-> {!r}".format(obj))
...
>>> import sys
>>> sys.displayhook = new_displayhook
>>> print_arg(10)
10
>>> return_arg(10)
-> 10
```

Understanding the difference between printing and returning is essential to
learning to use functions effectively, and tweaking the display of results
this way may help make the difference more obvious.


# Addendum: IPython (including IPython Notebook)

The initial examples above focused on the standard CPython runtime, include
the default interactive interpreter. The IPython interactive interpreter,
including the IPython Notebook, has a couple of interesting differences in
behaviour that are relevant to the above comments.

Firstly, it *does* display return values and printed values differently,
prefacing *results* with an output reference number:

```python
In [1]: print 10
10

In [2]: 10
Out[2]: 10
```

Secondly, it has an optional "autocall" feature that allows a user to tell
IPython to automatically add the missing parentheses to a function call if
the user leaves them out:

```sh
$ ipython3 --autocall=1 -c "print 10"
-> print(10)
10
```

This is a general purpose feature that allows users to make their IPython
sessions behave more like languages that don't have first class functions
(most notably, IPython's autocall feature closely resembles MATLAB's
"command syntax" notation for calling functions).

It also has the side effect that users that use IPython, have autocall
enabled, and don't use any of the more esoteric quirks of the Python 2
`print` statement (like stream redirection or suppressing the trailing
newline) may not even notice that `print` became an ordinary builtin in
Python 3.
