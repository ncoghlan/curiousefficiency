.. title: Why Python 4.0 won't be like Python 3.0
.. slug: python-4000
.. date: 2014-08-17 05:30:55 UTC
.. tags: python
.. link: 
.. description: 
.. type: text

Newcomers to python-ideas occasionally make reference to the idea of
"Python 4000" when proposing backwards incompatible changes that don't
offer a clear migration path from currently legal Python 3 code. After all,
we allowed that kind of change for Python 3.0, so why wouldn't we allow it
for Python 4.0?

I've heard that question enough times now (including the more concerned
phrasing "You made a big backwards compatibility break once, how do I know
you won't do it again?"), that I figured I'd record my answer here, so I'd
be able to refer people back to it in the future.

# What are the current expectations for Python 4.0?

My current expectation is that Python 4.0 will merely be "the release that
comes after Python 3.9". That's it. No profound changes to the language,
no major backwards compatibility breaks - going from Python 3.9 to 4.0
should be as uneventful as going from Python 3.3 to 3.4 (or from 2.6 to 2.7).
I even expect the stable Application Binary Interface (as first defined in
[PEP 384](https://www.python.org/dev/peps/pep-0384/)) to be preserved across
the boundary.

At the current rate of language feature releases (roughly every 18 months),
that means we would likely see Python 4.0 some time in 2023, rather than
seeing Python 3.10.

*Update:* After this post was originally written back in 2014, subsequent
discussions on the core python-dev mailing list led to the conclusion
that the release after 3.9 will probably just be 3.10. However, a 4.0
will presumably still happen some day, and the premise of this article
is expected to hold for that release: it will be held to the same backwards
compatibility obligations as a Python 3.X to 3.X+1 update.

# So how will Python continue to evolve?

First and foremost, nothing has changed about the Python Enhancement Proposal
process - backwards compatible changes are still proposed all the time, with
new modules (like `asyncio`) and language features (like `yield from`) being
added to enhance the capabilities available to Python applications. As time
goes by, Python 3 will continue to pull further ahead of Python 2 in terms
of the capabilities it offers by default, even if Python 2 users have access
to equivalent capabilities through third party modules or backports from
Python 3.

Competing interpreter implementations and extensions will also continue to
explore different ways of enhancing Python, including PyPy's exploration of
JIT-compiler generation and software transactional memory, and the
scientific and data analysis community's exploration of array oriented
programming that takes full advantage of the vectorisation capabilities
offered by modern CPUs and GPUs. Integration with other virtual machine
runtimes (like the JVM and CLR) is also expected to improve with time,
especially as the inroads Python is making in the education sector are likely
to make it ever more popular as an embedded scripting language in larger
applications running in those environments.

For backwards incompatible changes,
[PEP 387](https://www.python.org/dev/peps/pep-0387/) provides a reasonable
overview of the approach that was used for years in the Python 2 series, and
still applies today: if a feature is identified as being excessively
problematic, then it may be deprecated and eventually removed.

However, a number of other changes have been made to the development and
release process that make it less likely that such deprecations will be
needed within the Python 3 series:

* the greater emphasis on the Python Package Index, as indicated by the
  collaboration between the CPython core development team and the Python
  Packaging Authority, as well as the bundling of the `pip` installer with
  Python 3.4+, reduces the pressure to add modules to the standard library
  before they're sufficiently stable to accommodate the relatively slow
  language update cycle
* the "provisional API" concept (introduced in
  [PEP 411](https://www.python.org/dev/peps/pep-0411/)) makes it possible to
  apply a "settling in" period to libraries and APIs that are judged likely
  to benefit from broader feedback before offering the standard backwards
  compatibility guarantees
* a lot of accumulated legacy behaviour really was cleared out in the Python
  3 transition, and the requirements for new additions to Python and the
  standard library are *much* stricter now than they were in the Python 1.x
  and Python 2.x days
* the widespread development of "single source" Python 2/3 libraries and
  frameworks strongly encourages the use of "documented deprecation" in
  Python 3, even when features are replaced with newer, preferred,
  alternatives. In these cases, a deprecation notice is placed in the
  documentation, suggesting the approach that is preferred for new code,
  but no programmatic deprecation warning is added. This allows existing
  code, including code supporting both Python 2 and Python 3, to be left
  unchanged (at the expense of new users potentially having slightly more
  to learn when tasked with maintaining existing code bases).

# From (mostly) English to all written languages

It's also worth noting that Python 3 wasn't expected to be as disruptive as
it turned out to be. Of all the backwards incompatible changes in Python 3,
many of the serious barriers to migration can be laid at the feet of one
little bullet point in
[PEP 3100](https://www.python.org/dev/peps/pep-3100/#atomic-types):

* Make all strings be Unicode, and have a separate bytes() type. The new
  string type will be called 'str'.

PEP 3100 was the home for Python 3 changes that were considered sufficiently
non-controversial that no separate PEP was considered necessary. The reason
this particular change was considered non-controversial was because our
experience with Python 2 had shown that the authors of web and GUI frameworks
were right: dealing sensibly with Unicode as an *application* developer
means ensuring all text data is converted from binary as close to the system
boundary as possible, manipulated as text, and then converted back to binary
for output purposes.

Unfortunately, Python 2 doesn't encourage developers to write programs that
way - it blurs the boundaries between binary data and text extensively, and
makes it difficult for developers to keep the two separate in their heads,
let alone in their code. So web and GUI framework authors have to tell their
Python 2 users "always use Unicode text. If you don't, you may suffer from
obscure and hard to track down bugs when dealing with Unicode input".

Python 3 is different: it imposes a much greater separation between the
"binary domain" and the "text domain", making it easier to write normal
application code, while making it a bit harder to write code that works
with system boundaries where the distinction between binary and text data
can be substantially less clear. I've written in more detail
[elsewhere](https://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-actually-changed-in-the-text-model-between-python-2-and-python-3)
regarding what actually changed in the text model between Python 2 and
Python 3.

This revolution in Python's Unicode support is taking place against a larger
background migration of computational text manipulation from the English-only
[ASCII](https://en.wikipedia.org/wiki/ASCII) (officially defined in 1963),
through the complexity of the "binary data + encoding declaration" model
(including the [C/POSIX locale](https://en.wikipedia.org/wiki/Locale) and
[Windows code page](https://en.wikipedia.org/wiki/Windows_code_page)
systems introduced in the late 1980's) and the initial 16-bit only
version of the [Unicode standard](https://en.wikipedia.org/wiki/Unicode)
(released in 1991) to the relatively comprehensive modern Unicode code point
system (first defined in 1996, with new major updates released every few years).

Why mention this point? Because this switch to "Unicode by default" is the
most disruptive of the backwards incompatible changes in Python 3 and unlike
the others (which were more language specific), it is one small part of a
much larger industry wide change in how text data is represented and
manipulated. With the language specific issues cleared out by the Python 3
transition, a much higher barrier to entry for new language features compared
to the early days of Python and no other industry wide migrations on the
scale of switching from "binary data with an encoding" to Unicode for text
modelling currently in progress, I can't see any kind of change coming up
that would require a Python 3 style backwards compatibility break and
parallel support period. Instead, I expect we'll be able to accommodate any
future language evolution within the normal change management processes, and
any proposal that can't be handled that way will just get rejected as
imposing an unacceptably high cost on the community and the core development
team.
