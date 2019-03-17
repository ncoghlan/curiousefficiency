.. title: What does "x = a + b" mean?
.. slug: what-does-x-equals-a-plus-b-mean
.. date: 2019-03-16 06:06:21 UTC
.. tags: python
.. category: python
.. link:
.. description: Mathematical operators in programming language design
.. type: text

.. contents:: Making sense of "x = a + b"

Shorthand notations and shared context
--------------------------------------

Guido van Rossum recently put together an
`excellent post <https://neopythonic.blogspot.com/2019/03/why-operators-are-useful.html>`_
talking about the value of infix binary operators in making certain kinds of
operations easier to reason about correctly.

The context inspiring that post is a python-ideas discussion regarding the
possibility of adding a shorthand spelling (``x = a + b``) to Python for the
operation::

    x = a.copy()
    x.update(b)

The PEP for that proposal is still in development, so I'm not going to link to
it directly [#]_, but the paragraph above gives the gist of the idea. Guido's
article came in response to the assertion that infix operators don't improve
readability, when we have plenty of empirical evidence to show that they do.

Where *this* article comes from is a key point that Guido's article mentions,
but doesn't emphasise: that those readability benefits rely heavily on
implicitly shared context between the author of an expression and the readers
of that expression.

Without a previous agreement on the semantics, the only possible general answer
to the question "What does ``x = a + b`` mean?" is "I need more information to
answer that".


The original shared context: Algebra
------------------------------------

If the additional information supplied is "This is an algebraic expression",
then ``x = a + b`` is expressing a constraint on the permitted values of ``x``,
``a``, and ``b``.

Specifying ``x = a - b`` as an additional constraint would then further allow
the reader to infer that ``x = a`` and ``b = 0``.


The corresponding Python context: Numbers
-----------------------------------------

The use case for ``+`` in Python that most closely corresponds with algebra is
using it with numbers - the key differences lie in the meaning of ``=``, rather
than the meaning of ``+``.

So if the additional information supplied is "This is a Python assignment
statement; ``a`` and ``b`` are both well-behaved finite numbers", then the
reader will be able to infer that ``x`` will be the sum of the two numbers.

Inferring the exact numeric type of ``x`` would require yet more information
about the types of ``a`` and ``b``, as types implementing the numeric ``+``
operator are expected to participate in a type coercion protocol that gives
both operands a chance to carry out the operation, and only raises ``TypeError``
if neither type understands the other.

The original algebraic meaning then gets expressed in Python as
``assert x == a + b``, and successful execution of the assignment statement
ensures that assertion will pass.

In this context, types implementing the ``+`` operator are expected to provide
all the properties that would be expected of the corresponding mathematical
concepts (``a + b == b + a``, ``a + (b + c)  == (a + b) + c``, etc), subject
to the limitations of performing calculations on computers that actually exist.


Another mathematical context: Matrix algebra
--------------------------------------------

If the given expression used uppercase letters, as in ``X = A + B``, then the
additional information supplied may instead be "This is a matrix algebra
expression". (It's a notational convention in mathematics that matrices be
assigned uppercase letters, while lowercase letters indicate scalar values)

For matrices, addition and subtraction are defined as only being valid between
matrices of the same size and shape, so if ``X = A - B`` were to be supplied as
an additional constraint, then the implications would be:

* ``X``, ``A`` and ``B`` are all the same size and shape
* ``B`` consists entirely of zeroes
* ``X = A``


The corresponding Python context: NumPy Arrays
----------------------------------------------

The ``numpy.ndarray`` type, and other types implementing the same API, bring the
semantics of matrix algebra to Python programming, similar to the way that the
builtin numeric types bring the semantics of scalar algebra.

This means that if the additional information supplied is "This is a Python
assignment statement; ``A`` and ``B`` are both matrices of the same size and
shape containing well-behaved finite numbers", then the reader will be able to
infer that ``X`` will be a new matrix of the same shape and size as matrices
``A`` and ``B``, with each element in ``X`` being the sum of the corresponding
elements in ``A`` and ``B``.

As with scalar algebra, inferring the exact numeric type of the elements of
``X`` would require more information about the types of the elements in ``A``
and ``B``, the original algebraic meaning gets expressed in Python as
``assert X == A + B``, successful execution of the assignment statement
ensures that assertion will pass, and types implementing ``+`` in this context
are expected to provide the properties that would be expected of a matrix in
mathematics.


Python's string concatenation context
-------------------------------------

Mathematics doesn't provide a convenient infix notation for concatenating two
strings together (aside from writing their names directly next to each other),
so programming language designers are forced to choose one.

While this does vary across languages, the most common choice is the one that
Python uses: the ``+`` operator.

This is formally a distinct operation from numeric addition, with different
semantic expectations, and CPython's C API somewhat coincidentally ended up
reflecting that distinction by offering two different ways of implementing
``+`` on a type: the ``tp_number->nb_add`` and ``tp_sequence->sq_concat`` slots.
(This distinction is absent at the Python level: only ``__add__``, ``__radd__``
and ``__iadd__`` are exposed, and they always populate the relevant
``tp_number`` slots in CPython)

The key semantic difference between algebraic addition and string concatenation is
that in algebraic addition, the order of the operands doesn't matter
(``a + b == b + a``), while in the string concatenation case, the order of the
operands determines which items appear first in the result (e.g.
``"Hello" + "World" == "HelloWorld"`` vs ``"World" + "Hello" == "WorldHello"``).
This means that ``a + b == b + a`` being true when concatenating strings
indicates that either one or both strings are empty, or else the two strings are
identical.

Another less obvious semantic difference is that strings don't participate in
the type coercion protocol that is defined for numbers: if the right hand
operand isn't a string (or string subclass) instance, they'll raise
``TypeError`` immediately, rather than letting the other operand attempt the
operation.


Python's immutable sequence concatenation context
-------------------------------------------------

Python goes further than merely allowing ``+`` to be used for string
concatenation: it allows it to be used for arbitrary sequence concatenation.

For immutable container types like ``tuple``, this closely parallels the way
that string concatenation works: a new immutable instance of the same type is
created containing references to the same items referenced by the original
operands::

    >>> a = 1, 2, 3
    >>> b = 4, 5, 6
    >>> x = a + b
    >>> a
    (1, 2, 3)
    >>> b
    (4, 5, 6)
    >>> x
    (1, 2, 3, 4, 5, 6)

As for strings, immutable sequences will usually only interact with other
instances of the same type (or subclasses), even when the ``x += b`` notation
is used as an alternative to ``x = x + b``. For example::

    >>> x = 1, 2, 3
    >>> x += [4, 5, 6]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate tuple (not "list") to tuple
    >>> x += 4, 5, 6
    >>> x
    (1, 2, 3, 4, 5, 6)

In addition to ``str``, the ``tuple``, and ``bytes`` types implement these
concatenation semantics. ``range`` and ``memoryview``, while otherwise
implementing the ``Sequence`` API, don't support concatenation operations.


Python's mutable sequence concatenation context
-----------------------------------------------

Mutable sequence types add yet another variation to the possible meanings of
``+`` in Python. For the specific example of ``x = a + b``, they're very similar
to immutable sequences, creating a fresh instance that references the same items
as the original operands::

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> x = a + b
    >>> a
    [1, 2, 3]
    >>> b
    [4, 5, 6]
    >>> x
    [1, 2, 3, 4, 5, 6]

Where they diverge is that the ``x += b`` operation will modify the target
sequence directly, rather than creating a new container::

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> x = a; x = x + b
    >>> a
    [1, 2, 3]
    >>> x = a; x += b
    >>> a
    [1, 2, 3, 4, 5, 6]

The other difference is that where ``+`` remains restrictive as to the
container types it will work with, ``+=`` is typically generalised to work
with arbitrary iterables on the right hand side, just like the
``MutableMapping.extend()`` method::

    >>> x = [1, 2, 3]
    >>> x = x + (4, 5, 6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate list (not "tuple") to list
    >>> x += (4, 5, 6)
    >>> x
    [1, 2, 3, 4, 5, 6]

Amongst the builtins, ``list`` and ``bytearray`` implement these semantics
(although ``bytearray`` limits even in-place concatenation to ``bytes``-like
types that support ``memoryview`` style access). Elsewhere in the standard
library, ``collections.deque`` and ``array.array`` are other mutable sequence
types that behave this way.


A brief digression back to mathematics: Multisets
-------------------------------------------------

Multisets are a concept in mathematics that allow for values to occur in a set
more than once, with the multiset then being the mapping from the values
themselves to the count of how many times that value occurs in the multiset
(with a count of zero or less being the same as the value being omitted from
the set entirely).

While they don't natively use the ``x = a + b`` notation the way that scalar
algebra and matrix algebra do, the key point regarding multisets that's relevant
to this article is the fact that they do have a "Sum" operation defined, and the
semantics of that operation are very similar to those used for matrix addition:
element wise summation for each item in the multiset. If a particular value is
only present in one of the multisets, that's handled the same way as if it were
present with a count of zero.


And back to Python once more: ``collections.Counter``
-----------------------------------------------------

Since Python 2.7 and 3.1, Python has included an implementation of the
mathematical multiset concept in the form of the ``collections.Counter`` class.
It uses ``x = a + b`` to denote multiset summation::

    >>> a = collections.Counter(maths=2, python=2)
    >>> b = collections.Counter(python=4, maths=1)
    >>> x = a + b
    >>> x
    Counter({'python': 6, 'maths': 3})

As with sequences, counter instances define their own interoperability domain,
so they won't accept arbitrary mappings for a binary ``+`` operation::

    >>> x = a + dict(python=4, maths=1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'Counter' and 'dict'

But they're more permissive for in-place operations, accepting arbitrary
mapping objects::

    >>> x += dict(python=4, maths=1)
    >>> x
    Counter({'python': 10, 'maths': 4})


What does all this have to do with the idea of dictionary addition?
-------------------------------------------------------------------

Python's dictionaries are quite interesting mathematically, as in mathematical
terms, they're not actually a container. Instead, they're a function mapping
between a domain defined by the set of keys, and a range defined by a multiset
of values [#]_.

This means that the mathematical context that would most closely correspond to
defining addition on dictionaries is the algebraic combination of functions.
That's defined such that ``(f + g)(x)`` is equivalent to ``f(x) + g(x)``, so
the only binary in-fix operator support for dictionaries that could be grounded
in an existing mathematical shared context is one where ``d1 + d2`` was
shorthand for::

    x = d1.copy()
    for k, rhs in d2.items():
        try:
            lhs = x[k]
        except KeyError:
            x[k] = rhs
        else:
            x[k] = lhs + rhs

That has the unfortunate implication that introducing a Python-specific binary
operator shorthand for dictionary copy-and-update semantics would represent a
hard conceptual break with mathematics, rather than a transfer of existing
mathematical concepts into the language. Contrast that with the introduction
of ``collections.Counter`` (which was grounded in the semantics of mathematical
multisets and borrowed its Python notation from element-wise addition on
matrices), or the matrix multiplication operator (which was grounded in the
semantics of matrix algebra, and only needed a text-editor-friendly symbol
assigned, similar to using ``*`` instead of ``×`` for scalar multiplication
and ``/`` instead of ``÷`` for division),

At least to me, that seems like a big leap to take for something where the
in-place form already has a perfectly acceptable spelling (``d1.update(d2)``),
and a more expression-friendly variant could be provided as a new dictionary
class method::

    @classmethod
    def from_merge(cls, *inputs):
        self = cls()
        for input in inputs:
            self.update(input)
        return self

With that defined, then the exact equivalent of the proposed ``d1 + d2`` would
be ``type(d1).from_merge(d1, d2)``, and in practice, you would often give the
desired result type explicitly rather than inferring it from the inputs
(e.g. ``dict.from_merge(d1, d2)``).

However, the PEP is still in the very first stage of the discussion and review
process, so it's entirely possible that by the time it reaches ``python-dev``
it will be making a more modest proposal like a new ``dict`` class method,
rather than the current proposal of operator syntax support.

-----

.. [#] The whole point of the python-ideas phase of discussion is to get a PEP
   ready for a more critical review by the core development team, so it isn't
   fair to the PEP author to invite wider review before they're ready for it.

.. [#] The final section originally stated that arithmetic operations on
   mathematical functions didn't have a defined meaning, so proposing them for
   Python's dictionaries would be treading new conceptual ground. However, a
   `reader pointed out <https://twitter.com/deshipu/status/1107020770495086599>`_
   that algebraic operations on functions *are* defined, and they translate to
   applying the functions independently to the inputs, and then performing the
   specified arithmetic operation on the results. The final section has been
   updated accordingly.
