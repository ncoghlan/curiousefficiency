.. title: The transition to multilingual programming
.. slug: multilingual-programming
.. date: 2014-08-24 06:16:15 UTC
.. tags: python
.. link: 
.. description: 
.. type: text

A [recent thread](https://mail.python.org/pipermail/python-dev/2014-August/135873.html)
on python-dev prompted
[me to summarise](https://mail.python.org/pipermail/python-dev/2014-August/135977.html)
the current state of the ongoing industry wide transition from bilingual to
multilingual programming as it relates to Python's cross-platform support. It
also relates to the reasons why Python 3 turned out to be
[more disruptive](https://www.curiousefficiency.org/posts/2014/08/python-4000.html)
than the core development team initially expected.

A good starting point for anyone interested in exploring this topic further
is the ["Origin and development"](https://en.wikipedia.org/wiki/Unicode#Origin_and_development)
section of the Wikipedia article on Unicode, but I'll hit the key points
below.

# Monolingual computing

At their core, computers only understand single bits. Everything above that
is based on conventions that ascribe higher level meanings to particular
sequences of bits. One particular important set of conventions for
communicating between humans and computers are "text encodings": conventions
that map particular sequences of bits to text in the actual languages humans
read and write.

One of the oldest encodings still in common use is
[ASCII](https://en.wikipedia.org/wiki/ASCII) (which stands for "American
Standard Code for Information Interchange"), developed during the 1960's (it
just had its 50th birthday in 2013). This encoding maps the letters of the
English alphabet (in both upper and lower case), the decimal digits,
various punctuation characters and some additional "control codes" to the
128 numbers that can be encoded as a 7-bit sequence.

Many computer systems today still only work correctly with English - when
you encounter such a system, it's a fairly good bet that either the system
itself, or something it depends on, is limited to working with ASCII text.
(If you're *really* unlucky, you might even get to work with modal 5-bit
encodings like [ITA-2](https://en.wikipedia.org/wiki/ITA2#ITA2), as I have.
The legacy of the telegraph lives on!)

# Working with local languages

The first attempts at dealing with this limitation of ASCII simply assigned
meanings to the full range of 8-bit sequences. Known collectively as
"Extended ASCII", each of these systems allowed for an additional 128
characters, which was enough to handle many European and Cyrillic scripts.
Even 256 characters was nowhere near sufficient to deal with Indic
or East Asian languages, however, so this time also saw a proliferation of
ASCII incompatible encodings like ShiftJIS, ISO-2022 and Big5. This is why
Python ships with support for
[dozens of codecs](https://docs.python.org/3/library/codecs.html#standard-encodings)
from around the world.

This proliferation of encodings required a way to tell software which
encoding should be used to read the data. For protocols that were originally
designed for communication between computers, agreeing on a common text
encoding is usually handled as part of the protocol. In cases where no
encoding information is supplied (or to handle cases where there is a
mismatch between the claimed encoding and the actual encoding), then
applications may make use of "encoding detection" algorithms, like those
provided by the [chardet](https://pypi.python.org/pypi/chardet) package
for Python. These algorithms aren't perfect, but can give good answers when
given a sufficient amount of data to work with.

Local operating system interfaces, however, are a different story. Not
only don't they inherently convey encoding information, but the nature of
the problem is such that trying to use encoding detection isn't practical.
Two key systems arose in an attempt to deal with this problem:

* Windows code pages
* POSIX locale encodings

With both of these systems, a program would pick a code page or locale, and
use the corresponding text encoding to decide how to interpret text for
display to the user or combination with other text. This may include
deciding how to display information about the contents of the computer
itself (like listing the files in a directory).

The fundamental premise of these two systems is that the computer only needs
to speak the language of its immediate users. So, while the computer is
theoretically *capable* of communicating in any language, it can effectively
only communicate with humans in one language at a time. All of the data a
given application was working with would need to be in a *consistent*
encoding, or the result would be uninterpretable nonsense, something the
Japanese (and eventually everyone else) came to call
[mojibake](https://en.wikipedia.org/wiki/Mojibake).

It isn't a coincidence that the name for this concept came from an Asian
country: the encoding problems encountered there make the issues encountered
with European and Cyrillic languages look trivial by comparison.

Unfortunately, this "bilingual computing" approach (so called because the
computer could generally handle English in addition to the local language)
causes some serious problems once you consider communicating *between*
computers. While some of those problems were specific to network protocols,
there are some more serious ones that arise when dealing with nominally
"local" interfaces:

* networked computing meant one username might be used across multiple
  systems, including different operating systems
* network drives allow a single file server to be accessed from multiple
  clients, including different operating systems
* portable media (like DVDs and USB keys) allow the same filesystem to be
  accessed from multiple devices at different points in time
* data synchronisation services like Dropbox need to faithfully replicate
  a filesystem hierarchy not only across different desktop environments,
  but also to mobile devices

For these protocols that were originally designed only for local
interoperability communicating encoding information is generally difficult,
and it doesn't necessarily match the claimed encoding of the platform you're
running on.

# Unicode and the rise of multilingual computing

The path to addressing the fundamental limitations of bilingual computing
actually started more than 25 years ago, back in the late 1980's. An initial
draft proposal for a 16-bit "universal encoding" was released in 1988, the
[Unicode Consortium](https://en.wikipedia.org/wiki/Unicode_Consortium) was
formed in early 1991 and the first volume of the first version of
[Unicode](https://en.wikipedia.org/wiki/Unicode) was published later that
same year.

Microsoft added new text handling and operating system APIs to Windows based
on the 16-bit C level `wchar_t` type, and Sun also adopted Unicode as part
of the core design of Java's approach to handling text.

However, there was a problem. The original Unicode design had decided that
"16 bits ought to be enough for anybody" by restricting their target to
only modern scripts, and only frequently used characters within those
scripts. However, when you look at the "rarely used" Kanji and Han characters
for Japanese and Chinese, you find that they include many characters that
*are* regularly used for the names of people and places - they're just
largely restricted to proper nouns, and so won't show up in a normal
vocabulary search. So Unicode 2.0 was defined in 1996, expanding the system
out to a maximum of 21 bits per code point (using up to 32 bits per code
point for storage).

As a result, Windows (including the CLR) and Java now use the little-endian
variant of UTF-16 to allow their text APIs to handle arbitrary Unicode code
points. The original 16-bit code space is now referred to as the Basic
Multilingual Plane.

While all that was going on, the POSIX world ended up adopting a different
strategy for migrating to full Unicode support: attempting to standardise on
the ASCII compatible UTF-8 text encoding.

The choice between using UTF-8 and UTF-16-LE as the preferred local text
encoding involves some
[complicated trade-offs](https://en.wikipedia.org/wiki/UTF-8#Advantages_and_disadvantages),
and that's reflected in the fact that they have ended up being at the heart
of two competing approaches to multilingual computing.

Choosing UTF-8 aims to treat formatting text for communication with the user
as "just a display issue". It's a low impact design that will "just work" for
a lot of software, but it comes at a price:

* because encoding consistency checks are mostly avoided, data in different
  encodings may be freely concatenated and passed on to other applications.
  Such data is typically not usable by the receiving application.
* for interfaces without encoding information available, it is often
  necessary to assume an appropriate encoding in order to display information
  to the user, or to transform it to a different encoding for communication
  with another system that may not share the local system's encoding
  assumptions. These assumptions may not be correct, but won't necessarily
  cause an error - the data may just be silently misinterpreted as something
  other than what was originally intended.
* because data is generally decoded far from where it was introduced, it
  can be difficult to discover the origin of encoding errors.
* as a variable width encoding, it is more difficult to develop efficient
  string manipulation algorithms for UTF-8. Algorithms originally designed
  for fixed width encodings will no longer work.
* as a specific instance of the previous point, it isn't possible to split
  UTF-8 encoded text at arbitrary locations. Care needs to be taken to ensure
  splits only occur at code point boundaries.

UTF-16-LE shares the last two problem, but to a lesser degree (simply due to
the fact most commonly used code points are in the 16-bit Basic Multilingual
Plane). However, because it *isn't* generally suitable for use in network
protocols and file formats (without significant additional encoding markers),
the explicit decoding and encoding required encourages designs with a clear
separation between binary data (including encoded text) and decoded text
data.

# Through the lens of Python

Python and Unicode were born on opposites side of the Atlantic ocean at
roughly the same time (1991). The growing adoption of Unicode within the
computing industry has had a profound impact on the evolution of the
language.

Python 1.x was purely a product of the bilingual computing era - it had no
support for Unicode based text handling at all, and was hence largely
limited to 8-bit ASCII compatible encodings for text processing.

Python 2.x was still primarily a product of the bilingual era, but added
multilingual support as an optional addon, in the form of the `unicode`
type and support for a wide variety of text encodings.
[PEP 100](https://www.python.org/dev/peps/pep-0100/) goes into the many
technical details that needed to be covered in order to incorporate that
feature. With Python 2, you *can* make multilingual programming work, but
it requires an active decision on the part of the application developer,
or at least that they follow the guidelines of a framework that handles the
problem on their behalf.

By contrast, Python 3.x is designed to be a native denizen of the
multilingual computing world. Support for multiple languages extends as far
as the variable naming system, such that languages other than English become
almost as well supported as English already was in Python 2. While the
English inspired keywords and the English naming in the standard library and
on the Python Package Index mean that Python's "native" language and the
preferred language for global collaboration will always be English, the new
design allows a lot more flexibility when working with data in other
languages.

Consider processing a data table where the headings are names of Japanese
individuals, and we'd like to use `collections.namedtuple` to process
each row. Python 2 simply can't handle this task:

```python
>>> from collections import namedtuple
>>> People = namedtuple("People", u"陽斗 慶子 七海")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python2.7/collections.py", line 310, in namedtuple
    field_names = map(str, field_names)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

Users need to either restrict themselves to dictionary style lookups rather
than attribute access, or else used romanised versions of their names
(Haruto, Keiko, Nanami for the example). However, the case of "Haruto" is an
interesting one, as there at least 3 *different* ways of writing that as
Kanji (陽斗, 陽翔, 大翔), but they are all romanised as the same string
(Haruto). If you try to use romaaji to handle a data set that contains
more than one variant of that name, you're going to get spurious collisions.

Python 3 takes a very different perspective on this problem. It says it
should just work, and it makes sure it does:

```python
>>> from collections import namedtuple
>>> People = namedtuple("People", u"陽斗 慶子 七海")
>>> d = People(1, 2, 3)
>>> d.陽斗
1
>>> d.慶子
2
>>> d.七海
3
```

This change greatly expands the kinds of "data driven" use cases Python can
support in areas where the ASCII based assumptions of Python 2 would cause
serious problems.

Python 3 still needs to deal with improperly encoded data however, so it
provides a mechanism for arbitrary binary data to be "smuggled" through
text strings in the Unicode Private Use Area. This feature was added by
[PEP 383](https://www.python.org/dev/peps/pep-0383/) and is managed through
the `surrogateescape` error handler, which is used by default on most
operating system interfaces. This recreates the old Python 2 behaviour of
passing improperly encoded data through unchanged when dealing solely with
local operating system interfaces, but complaining when such improperly
encoded data is injected into another interface. The codec error handling
system provides several tools to deal with these files, and we're looking
at adding a few more relevant convenience functions for Python 3.5.

The underlying Unicode changes in Python 3 also made
[PEP 393](https://www.python.org/dev/peps/pep-0393/) possible, which changed
the way the CPython interpreter stores text internally. In Python 2, even
pure ASCII strings would consume four bytes per code point on Linux systems.
Using the "narrow build" option (as the Python 2 Windows builds from
python.org do) reduced that the only two bytes per code point when operating
within the Basic Multilingual Plane, but at the cost of potentially producing
*wrong answers* when asked to operate on code points outside the Basic
Multilingual Plane. By contrast, starting with Python 3.3, CPython now
stores text internally using the smallest fixed width data unit possible.
That is, `latin-1` text uses 8 bits per code point, `UCS-2` (Basic
Multilingual Plane) text uses 16-bits per code point, and only text
containing code points outside the Basic Multilingual Plane will expand to
needing the full 32 bits per code point. This can not only significantly
reduce the amount of memory needed for multilingual applications, but may
also increase their speed as well (as reducing memory usage also reduces
the time spent copying data around).

# Are we there yet?

In a word, no. Not for Python 3.4, and not for the computing industry at
large. We're much closer than we ever have been before, though. Most
POSIX systems now default to UTF-8 as their default encoding, and many
systems offer a `C.UTF-8` locale as an alternative to the traditional
ASCII based `C` locale. When dealing solely with properly encoded data and
metadata, and properly configured systems, Python 3 should "just work", even
when exchanging data between different platforms.

For Python 3, the remaining challenges fall into a few areas:

* helping existing Python 2 users adopt the optional multilingual features
  that will prepare them for eventual migration to Python 3 (as well as
  reassuring those users that don't wish to migrate that Python 2 is still
  fully supported, and will remain so for at least the next several years,
  and potentially longer for customers of commercial redistributors)
* adding back some features for working entirely in the binary domain that
  were removed in the original Python 3 transition due to an initial
  assessment that they were operations that only made sense on text data
  ([PEP 361](https://www.python.org/dev/peps/pep-0361/) summary:
  `bytes.__mod__` is coming back in Python 3.5 as a valid binary domain
  operation, `bytes.format` stays gone as an operation that only makes sense
  when working with actual text data)
* better handling of improperly decoded data, including poor encoding
  recommendations from the operating system (for example, Python 3.5 will
  be more sceptical when the operating system tells it the preferred encoding
  is `ASCII` and will enable the `surrogateescape` error handler on
  `sys.stdout` when it occurs)
* eliminating most remaining usage of the legacy code page and locale
  encoding systems in the CPython interpreter (this most notably affects the
  Windows console interface and argument decoding on POSIX. While these
  aren't easy problems to solve, it will still hopefully be possible to
  address them for Python 3.5)

More broadly, each major platform has its own significant challenges to
address:

* for POSIX systems, there are still a lot of systems that don't use UTF-8
  as the preferred encoding and the assumption of ASCII as the preferred
  encoding in the default `C` locale is positively archaic. There is
  also still a lot of POSIX software that still believes in the "text is
  just encoded bytes" assumption, and will happily produce mojibake that
  makes no sense to other applications or systems.
* for Windows, keeping the old 8-bit APIs around was deemed necessary for
  backwards compatibility, but this also means that there is still a lot of
  Windows software that simply doesn't handle multilingual computing
  correctly.
* for both Windows and the JVM, a fair amount of nominally multilingual
  software actually only works correctly with data in the basic multilingual
  plane. This is a smaller problem than not supporting multilingual computing
  at all, but was quite a noticeable problem in Python 2's own Windows
  support.

Mac OS X is the platform most tightly controlled by any one entity (Apple),
and they're actually in the best position out of all of the current major
platforms when it comes to handling multilingual computing correctly. They've
been one of the major drivers of Unicode since the beginning (two of the
authors of the initial Unicode proposal were Apple engineers), and were able
to force the necessary configuration changes on all their systems, rather
than having to work with an extensive network of OEM partners (Windows,
commercial Linux vendors) or relatively loose collaborations of individuals
and organisations (community Linux distributions).

Modern mobile platforms are generally in a better position than desktop
operating systems, mostly by virtue of being newer, and hence defined after
Unicode was better understood. However, the UTF-8 vs UTF-16-LE distinction
for text handling exists even there, thanks to the Java inspired Dalvik VM
in Android (plus the cloud-backed nature of modern smartphones means you're
even *more* likely to be encounter files from multiple machines when working
on a mobile device).
