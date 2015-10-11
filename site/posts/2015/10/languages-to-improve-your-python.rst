.. title: 27 languages to improve your Python
.. slug: languages-to-improve-your-python
.. date: 2015-09-06 02:54:39 UTC
.. tags: python
.. category: python
.. link: 
.. description: 27 programming languages that may improve your Python skills
.. type: text

.. contents:: 27 Languages

As a co-designer of one of the world's most popular programming languages, one
of the more frustrating behaviours I regularly see (both in the Python community
and in others) is influential people trying to tap into fears of "losing" to
other open source communities as a motivating force for community contributions.
(I'm occasionally guilty of this misbehaviour myself, which makes it even
easier to spot when others are falling into the same trap).

While learning from the experiences of other programming language communities
is a good thing, fear based approaches to motivating action are seriously
problematic, as they encourage community members to see members of those
other communities as enemies in a competition for contributor attention, rather
than as potential allies in the larger challenge of advancing the state of the
art in software development. It also has the effect of telling folks that enjoy
those other languages that they're not welcome in a community that views them
and their peers as "hostile competitors".

In truth, we *want* there to be a rich smorgasboard of cross platform open
source programming languages to choose from, as programming languages are first
and foremost *tools for thinking* - they make it possible for us to convey our
ideas in terms so explicit that even a computer can understand them. If someone
has found a language to use that fits their brain and solves their immediate
problems, *that's great*, regardless of the specific language (or languages)
they choose.

So I have three specific requests for the Python community, and one broader
suggestion. First, the specific requests:

1. If we find it necessary to appeal to tribal instincts to motivate action, we
   should avoid using tribal fear, and instead aim to use tribal pride.
   When we use fear as a motivator, as in phrasings like "If we don't do X,
   we're going to lose developer mindshare to language Y", we're deliberately
   creating negative emotions in folks freely contributing the results of their
   work to the world at large. Relying on tribal pride instead leads to
   phrasings like "It's currently really unclear how to solve problem X in
   Python. If we look to ecosystem Y, we can see they have a really nice
   approach to solving problem X that we can potentially adapt to provide a
   similarly nice user experience in Python". Actively emphasising taking pride
   in our own efforts, rather than denigrating the efforts of others, helps
   promote a culture of continuous learning within the Python community and
   also encourages the development of ever improving collaborative
   relationships with other communities.
2. Refrain from adopting attitudes of contempt towards other open source
   programming language communities, *especially* if those communities have
   empowered people to solve their own problems rather than having to wait for
   commercial software vendors to deign to address them. Most of the important
   problems in the world aren't profitable to solve (as the folks afflicted by
   them aren't personally wealthy and don't control institutional funding
   decisions), so we should be encouraging and applauding the folks stepping up
   to try to solve them, regardless of what we may think of their technology
   choices.
3. If someone we know is learning to program for the first time, and they
   choose to learn a language we don't personally like, we should *support them
   in their choice anyway*. They know what fits *their* brain better than we do,
   so the right language for us you may not be the right language for them. If
   they start getting frustrated with their original choice, to the point where
   it's demotivating them from learning to program at all, *then* it makes sense
   to start recommending alternatives. This advice applies even for those of us
   involved in improving the tragically bad state of network security: the way
   we solve the problem with inherently insecure languages is by improving
   operating system sandboxing capabilities, progressively knocking down
   barriers to adoption for languages with better native security properties,
   and improving the default behaviours of existing languages, not by confusing
   beginners with arguments about why their chosen language is a poor choice
   from an application security perspective. (If folks are deploying unaudited
   software written by beginners to handle security sensitive tasks, it isn't
   the folks *writing* the software that are the problem, it's the folks
   deploying it without performing appropriate due diligence on the provenance
   and security properties of that software)

My broader suggestion is aimed at folks that are starting to encounter the
limits of the core procedural subset of Python and would hence like to start
exploring more of Python's own available "tools for thinking".

One of the things we do as part of the Python core development process is to
look at features we appreciate having available in other languages we have
experience with, and see whether or not there is a way to adapt them to be
useful in making Python code easier to both read and write. This means that
learning another programming language that focuses more specifically on a
given style of software development can help improve *anyone's* understanding
of that style of programming in the context of Python.

To aid in such efforts, I've provided a list below of some possible areas for
exploration, and other languages which may provide additional insight into
those areas. Where possible, I've linked to Wikipedia pages rather than
directly to the relevant home pages, as Wikipedia often provides interesting
historical context that's worth exploring when picking up a new programming
language as an educational exercise rather than for immediate practical use.

While I do know many of these languages personally (and have used several of
them in developing production systems), the full list of recommendations
includes additional languages that I only know indirectly (usually by either
reading tutorials and design documentation, or by talking to folks that I trust
to provide good insight into a language's strengths and weaknesses).

There are a `lot of other languages`_ that could have gone on this list, so the
specific ones listed are a somewhat arbitrary subset based on my own interests
(for example, I'm mainly interested in the dominant Linux, Android and Windows
ecosystems, so I left out the niche-but-profitable Apple-centric Objective-C
and Swift programming languages, and I'm not familiar enough with art-focused
environments like `Processing`_ to even guess at what learning them might teach
a Python developer). For a more complete list that takes into account factors
beyond what a language might teach you as a developer, IEEE Spectrum's
`annual ranking`_ of programming language popularity and growth is well worth a
look.

.. _lot of other languages: https://github.com/mame/quine-relay
.. _Objective-C: https://en.wikipedia.org/wiki/Objective-C
.. _Swift: https://en.wikipedia.org/wiki/Swift_%28programming_language%29
.. _Processing: https://en.wikipedia.org/wiki/Processing_%28programming_language%29
.. _annual ranking: http://spectrum.ieee.org/static/interactive-the-top-programming-languages-2015


Procedural programming: C, Rust, Cython
---------------------------------------

Python's default execution model is procedural: we start at the top of the main
module and execute it statement by statement. All of Python's support for the
other approaches to data and computational modelling covered below are built
on this procedural foundation.

The `C`_ programming language is still the unchallenged ruler of low level
procedural programming. It's the core implementation language for the reference
Python interpreter, and also for the Linux operating system kernel. As a
software developer, learning C is one of the best ways to start learning more
about the underlying hardware that executes software applications - C is often
described as "portable assembly language", and one of the first applications
cross-compiled for any new CPU architecture will be a C compiler

`Rust`_, by contrast, is a relatively new programming language created by
Mozilla. The reason it makes this list is because Rust aims to take all of the
lessons we've learned as an industry regarding what *not* to do in C, and
design a new language that is interoperable with C libraries, offers the same
precise control over hardware usage that is needed in a low level systems
program language, but uses a different compile time approach to data modelling
and memory management to structurally eliminate many of the common flaws
afflicting C programs (such as buffer overflows, double free errors, null
pointer access, and thread synchronisation problems). I'm an embedded systems
engineer by training and initial professional experience, and Rust is the first
new language I've seen that looks like it may have the potential to scale down
to all of the niches currently dominated by C and custom assembly code.

`Cython`_ is also a lower level procedural-by-default language, but unlike
general purpose languages like C and Rust, Cython is aimed specifically at
writing CPython extension modules. To support that goal, Cython is designed as
a Python superset, allowing the programmer to choose when to favour the pure
Python syntax for flexibility, and when to favour Cython's syntax extensions
that make it possible to generate code that is equivalent to native C code in
terms of speed and memory efficiency.

Learning one of these languages is likely to provide insight into memory
management, algorithmic efficiency, binary interface compatibility, software
portability, and other practical aspects of turning source code into running
systems.

.. _C: https://en.wikipedia.org/wiki/C_%28programming_language%29
.. _Rust: https://en.wikipedia.org/wiki/Rust_%28programming_language%29
.. _Cython: https://en.wikipedia.org/wiki/Cython


Object-oriented data modelling: Java, C#, Eiffel
------------------------------------------------

One of the main things we need to do in programming is to model the state of
the real world, and offering native syntactic support for object-oriented
programming is one of the most popular approaches for doing that:
structurally grouping data structures, and methods for operating on those
data structures into classes.

Python itself is deliberately designed so that it is possible to *use* the
object-oriented features without first needing to learn to write your own
classes. Not every language adopts that approach - those listed in this section
are ones that consider learning object-oriented design to be a requirement for
using the language at all.

After a major marketing push by Sun Microsystems in the mid-to-late 1990's,
`Java`_ became the default language for teaching introductory computer science
in many tertiary institutions. While it is now being displaced by Python for
many educational use cases, it remains one of the most popular languages for
the development of business applications. There are a range of other languages
that target the common JVM (Java Virtual Machine) runtime, including the
Jython implementation of Python. The Dalvik and ART environments for Android
systems are based on a reimplementation of the Java programming APIs.

`C#`_ is similar in many ways to Java, and emerged as an alternative after Sun
and Microsoft failed to work out their business differences around Microsoft's
Java implementation, `J++`_. Like Java, it's a popular language for the
development of business applications, and there are a range of other languages
that target the shared .NET CLR (Common Language Runtime), including
the IronPython implementation of Python (the core components of the original
IronPython 1.0 implementation were extracted to create the language neutral
.NET Dynamic Language Runtime). For a long time, .NET was a proprietary Windows
specific technology, with `mono`_ as a cross-platform open source
reimplementation, but Microsoft shifted to an `open source ecosystem strategy`_
in early 2015.

Unlike most of the languages in this list, `Eiffel`_ isn't one I'd recommend
for practical day-to-day use. Rather, it's one I recommend because learning it
taught *me* an incredible amount about good object-oriented design where
"verifiably correct" is a design goal for the application. (Learning Eiffel also
taught me a lot about why "verifiably correct" isn't actually a design goal in
most software development, as verifiably correct software really doesn't cope
well with ambiguity and is entirely unsuitable for cases where you genuinely
don't know the relevant constraints yet and need to leave yourself enough
wiggle room to be able to figure out the finer details through iterative
development).

Learning one of these languages is likely to provide insight into inheritance
models, design-by-contract, class invariants, pre-conditions, post-conditions,
covariance, contravariance, method resolution order, generic programming, and
various other notions that also apply to Python's type system. There are also
a number of standard library modules and third party frameworks that use this
"visibly object-oriented" design style, such as the ``unittest`` and ``logging``
modules, and class-based views in the ``Django`` web framework.

.. _Java: https://en.wikipedia.org/wiki/Java_%28programming_language%29
.. _C#: https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29
.. _J++: https://en.wikipedia.org/wiki/Visual_J%2B%2B
.. _Eiffel: https://en.wikipedia.org/wiki/Eiffel_%28programming_language%29
.. _mono: https://en.wikipedia.org/wiki/Mono_%28software%29
.. _open source ecosystem strategy: http://radar.oreilly.com/2015/06/net-open-source.html


Object-oriented C derivatives: C++, D
-------------------------------------

One way of using the CPython runtime is as a "C with objects" programming
environment - at its core, CPython is implemented using C's approach to
object-oriented programming, which is to define C ``structs`` to hold the data
of interest, and to pass in instances of the struct as the first argument to
functions that then manipulate that data (these are the omnipresent
``PyObject*`` pointers in the CPython C API). This design pattern is
deliberately mirrored at the Python level in the form of the explicit ``self``
and ``cls`` arguments to instance methods and class methods.

`C++`_ is a programming language that aimed to retain full source compatibility
with ``C``, while adding higher level features like native object-oriented
programming support and template based metaprogramming. It's notoriously verbose
and hard to program in (although the 2011 update to the language standard
addressed many of the worst problems), but it's also the language of choice in
many contexts, including 3D modelling graphics engines and cross-platform
application development frameworks like Qt.

The `D`_ programming language is also interesting, as it has a similar
relationship to C++ as Rust has to C: it aims to keep most of the desirable
characteristics of C++, while also avoiding many of its problems (like the lack
of memory safety). Unlike Rust, D was not a ground up design of a new
programming language from scratch - instead, D is a close derivative of C++,
and while it isn't a strict C superset as C++ is, it does follow the design
principle that any code that falls into the common subset of C and D must
behave the same way in both languages.

Learning one of these languages is likely to provide insight into the
complexities of combining higher level language features with the underlying
C runtime model. Learning C++ is also likely to be useful when using Python
to manipulate existing libraries and toolkits written in C++.

.. _C++: https://en.wikipedia.org/wiki/C%2B%2B
.. _D: https://en.wikipedia.org/wiki/D_%28programming_language%29


Array-oriented data processing: MATLAB/Octave, Julia
----------------------------------------------------

Array oriented programming is designed to support numerical programming models:
those based on matrix algebra and related numerical methods.

While Python's standard library doesn't support this directly, array oriented
programming *is* taken into account in the language design, with a range of
syntactic and semantic features being added specifically for the benefit of
the third party `NumPy`_ library and similarly array-oriented tools.

In many cases, the `Scientific Python`_ stack is adopted as an alternative to
the proprietary `MATLAB`_ programming environment, which is used extensively
for modelling, simulation and numerical data analysis in science and
engineering. `GNU Octave`_ is an open source alternative that aims to be
syntactically compatible with MATLAB code, allowing folks to compare and
contrast the two approaches to array-oriented programming.

`Julia`_ is another relatively new language, which focuses heavily on array
oriented programming and type-based function overloading.

Learning one of these languages is likely to provide insight into the
capabilities of the Scientific Python stack, as well as providing opportunities
to explore hardware level parallel execution through technologies like OpenCL
and Nvidia's CUDA, and distributed data processing through ecosystems like
`Apache Spark`_ and the Python-specific `Blaze`_.

.. _NumPy: https://en.wikipedia.org/wiki/NumPy
.. _Scientific Python: https://en.wikipedia.org/wiki/SciPy
.. _MATLAB: https://en.wikipedia.org/wiki/MATLAB
.. _GNU Octave: https://en.wikipedia.org/wiki/GNU_Octave
.. _Julia: https://en.wikipedia.org/wiki/Julia_%28programming_language%29
.. _OpenCL: https://en.wikipedia.org/wiki/OpenCL
.. _CUDA: https://en.wikipedia.org/wiki/CUDA
.. _Apache Spark: https://spark.apache.org/
.. _Blaze: http://blaze.pydata.org/


Statistical data analysis: R
----------------------------

As access to large data sets has grown, so has demand for capable freely
available analytical tools for processing those data sets. One such tool is
the `R`_ programming language, which focuses specifically on statistical data
analysis and visualisation.

Learning R is likely to provide insight into the statistical analysis
capabilities of the Scientific Python stack, especially the `pandas`_ data
manipulation library and the `seaborn`_ statistical visualisation library.

.. _R: https://en.wikipedia.org/wiki/R_%28programming_language%29
.. _pandas: https://en.wikipedia.org/wiki/Pandas_%28software%29
.. _seaborn: http://stanford.edu/~mwaskom/software/seaborn/


Computational pipeline modelling: Haskell, Scala, Clojure, F#
-------------------------------------------------------------

Object-oriented data modelling and array-oriented data processing focus a lot
of attention on modelling data at rest, either in the form of collections of
named attributes or as arrays of structured data.

By contrast, functional programming languages emphasise the modelling of data
in motion, in the form of computational flows. Learning at least the basics
of functional programming can help greatly improve the structure of data
transformation operations even in otherwise procedural, object-oriented or
array-oriented applications.

`Haskell`_ is a functional programming language that has had a significant
influence on the design of Python, most notably through the introduction of
`list comprehensions`_ in Python 2.0.

`Scala`_ is an (arguably) functional programming language for the JVM that,
together with Java, Python and R, is one of the four primary programming
languages for the Apache Spark data analysis platform. While being designed to
encourage functional programming approaches, Scala's syntax, data model, and
execution model are also designed to minimise barriers to adoption for current
Java programmers (hence the "arguably" - the case can be made that Scala is
better categorised as an object-oriented programming language with strong
functional programming support).

`Clojure`_ is another functional programming language for the JVM that is
designed as a dialect of `Lisp`_. It earns its place in this list by being
the inspiration for the `toolz`_ functional programming toolkit for Python.

`F#`_ isn't a language I'm particularly familiar with myself, but seems worth
noting as the preferred functional programming language for the .NET CLR.

Learning one of these languages is likely to provide insight into Python's own
computational pipeline modelling tools, including container comprehensions,
generators, generator expressions, the ``functools`` and ``itertools`` standard
library modules, and third party functional Python toolkits like ``toolz``.

.. _Haskell: https://en.wikipedia.org/wiki/Haskell_%28programming_language%29
.. _list comprehensions: https://docs.python.org/3/whatsnew/2.0.html#list-comprehensions
.. _Scala: https://en.wikipedia.org/wiki/Scala_%28programming_language%29
.. _Clojure: https://en.wikipedia.org/wiki/Clojure
.. _Lisp: https://en.wikipedia.org/wiki/Lisp_%28programming_language%29
.. _F#: https://en.wikipedia.org/wiki/F_Sharp_%28programming_language%29
.. _toolz: https://toolz.readthedocs.org/en/latest/heritage.html


Event driven programming: JavaScript, Go, Erlang, Elixir
--------------------------------------------------------

Computational pipelines are an excellent way to handle data transformation and
analysis problems, but many problems require that an application run as a
persistent service that *waits* for events to occur, and then *handles* those
events. In these kinds of services, it is usually essential to be able to handle
multiple events concurrently in order to be able to accommodate multiple users
(or at least multiple actions) at the same time.

`JavaScript`_ was originally developed as an event handling language for web
browsers, permitting website developers to respond locally to client side
actions (such as mouse clicks and key presses) and events (such as the page
rendering being completed). It is supported in all modern browsers, and
together with the HTML5 Domain Object Model, has become a de facto standard
for defining the appearance and behaviour of user interfaces.

`Go`_ was designed by Google as a purpose built language for creating highly
scalable web services, and has also proven to be a very capable language for
developing command line applications. The most interesting aspect of Go from
a programming language design perspective is its use of `Communicating
Sequential Processes`_ concepts in its core concurrency model.

`Erlang`_ was designed by Ericsson as a purpose built language for creating
highly reliable telephony switches and similar devices, and is the language
powering the popular `RabbitMQ`_ message broker. Erlang uses the `Actor model`_
as its core concurrency primitive, passing messages between threads of
execution, rather than allowing them to share data directly. While I've never
programmed in Erlang myself, my first full-time job involved working with (and
on) an Actor-based concurrency framework for C++ developed by an ex-Ericsson
engineer, as well as developing such a framework myself based on the TSK (Task)
and MBX (Mailbox) primitives in Texas Instrument's lightweight `DSP/BIOS`_
runtime (now known as TI-RTOS).

`Elixir`_ earns an entry on the list by being a language designed to run on the
Erlang VM that exposes the same concurrency semantics as Erlang, while also
providing a range of additional language level features to help provide a more
well-rounded environment that is more likely to appeal to developers migrating
from other languages like Python, Java, or Ruby.

Learning one of these languages is likely to provide insight into Python's own
concurrency and parallelism support, including native coroutines, generator
based coroutines, the ``concurrent.futures`` and ``asyncio`` standard
library modules, third party network service development frameworks like
`Twisted`_ and `Tornado`_, the `channels`_ concept being introduced to Django,
and the event handling loops in GUI frameworks.

.. _JavaScript: https://en.wikipedia.org/wiki/JavaScript
.. _Go: https://en.wikipedia.org/wiki/Go_%28programming_language%29
.. _Communicating Sequential Processes: https://en.wikipedia.org/wiki/Communicating_sequential_processes
.. _Erlang: https://en.wikipedia.org/wiki/Erlang_%28programming_language%29
.. _RabbitMQ: https://en.wikipedia.org/wiki/RabbitMQ
.. _Actor model: https://en.wikipedia.org/wiki/Actor_model
.. _DSP/BIOS: https://en.wikipedia.org/wiki/TI-RTOS
.. _Elixir: https://en.wikipedia.org/wiki/Elixir_%28programming_language%29
.. _Twisted: https://en.wikipedia.org/wiki/Twisted_%28software%29
.. _Tornado: https://en.wikipedia.org/wiki/Tornado_%28web_server%29
.. _channels: http://channels.readthedocs.org/en/latest/concepts.html


Gradual typing: TypeScript
--------------------------

One of the more controversial features that landed in Python 3.5 was the new
``typing`` module, which brings a standard lexicon for gradual typing support
to the Python ecosystem.

For folks whose primary exposure to static typing is in languages like C,
C++ and Java, this seems like an astoundingly terrible idea (hence the
controversy).

Microsoft's `TypeScript`_, which provides gradual typing for JavaScript
applications provides a better illustration of the concept. TypeScript code
compiles to JavaScript code (which then doesn't include any runtime type
checking), and TypeScript annotations for popular JavaScript libraries are
maintained in the dedicated `DefinitelyTyped`_ repository.

As Chris Neugebaur pointed out in his `PyCon Australia presentation`_, this is
very similar to the proposed relationship between Python, the `typeshed`_ type
hint repository, and type inference and analysis tools like `mypy`_.

In essence, bothTypeScript and type hinting in Python are ways of writing
particular kinds of tests, either as separate files (just like normal tests),
or inline with the main body of the code (just like type declarations in
statically typed languages). In either case, you run a *separate* command to
actually check that the rest of the code is consistent with the available type
assertions (this occurs implicitly as part of the compilation to JavaScript for
TypeScript, and as an entirely optional static analysis task for Python's type
hinting).

.. _TypeScript: https://en.wikipedia.org/wiki/TypeScript
.. _DefinitelyTyped: http://definitelytyped.org/
.. _PyCon Australia presentation: https://www.youtube.com/watch?v=_PPQLeimyOM
.. _typeshed: https://github.com/python/typeshed
.. _mypy: http://mypy-lang.org/


Dynamic metaprogramming: Hy, Ruby
---------------------------------

A feature folks coming to Python from languages like C, C++, C# and Java often
find disconcerting is the notion that "code is data": the fact that things like
functions and classes are runtime objects that can be manipulated like any
other object.

`Hy`_ is a Lisp dialect that runs on both the CPython VM and the PyPy VM. Lisp
dialects take the "code as data" concept to extremes, as Lisp code consists of
nested lists describing the operations to be performed (the name of the language
itself stands for "LISt Processor"). The great strength of Lisp-style languages
is that they make it incredibly easy to eliminate write your own domain specific
languages. The great weakness of Lisp-style languages is that they make it
incredibly easy to write your own domain specific languages, which can sometimes
make it difficult to read other people's code.

`Ruby`_ is a language that is similar to Python in many respects, but as a
community is far more open to making use of dynamic metaprogramming features
that are "supported, but not encouraged" in Python. This includes things like
reopening class definitions to add additional methods, and using closures to
implement core language constructs like iteration.

Learning one of these languages is likely to provide insight into Python's own
dynamic metaprogramming support, including function and class decorators,
`monkeypatching`_, the ``unittest.mock`` standard library module, and third
party object proxying modules like `wrapt`_. (I'm not aware of any languages to
learn that are likely to provide insight into Python's metaclass system, so if
anyone has any suggestions on that front, please mention them in the comments.
Metaclasses power features like the core type system, abstract base classes,
enumeration types and runtime evaluation of gradual typing expressions)

.. _Hy: https://en.wikipedia.org/wiki/Hy
.. _Ruby: https://en.wikipedia.org/wiki/Ruby_%28programming_language%29
.. _monkeypatching: https://en.wikipedia.org/wiki/Monkey_patch
.. _wrapt: http://wrapt.readthedocs.org/en/latest/


Pragmatic problem solving: Lua, PHP, Perl
-----------------------------------------

Popular programming languages don't exist in isolation - they exist as part of
larger ecosystems of redistributors (both commercial and community focused),
end users, framework developers, tool developers, educators and more.

`Lua`_ is a popular programming language for embedding in a larger applications
as a scripting engine. Significant examples include it being the language
used to write add-ons for the World of Warcraft game client, and it's also
embedded in the RPM utility used by many Linux distributions. Compared to
CPython, a Lua runtime will generally be a tenth of the size, and it's weaker
introspection capabilities generally make it easier to isolate from the rest of
the application and the host operating system. A notable contribution from the
Lua community to the Python ecosystem is the adoption of the LuaJIT FFI
(Foreign Function Interface) as the basis of the JIT-friendly `cffi`_ interface
library for CPython and PyPy.

`PHP`_ is another popular programming language that rose to prominence as the
original "P" in the Linux-Apache-MySQL-PHP `LAMP stack`_, due to its focus on
producing HTML pages, and its broad availability on early Virtual Private
Server hosting providers. For all the handwringing about conceptual flaws in
various aspects of its design, it's now the basis of several widely popular
open source web services, including the Drupal content management system, the
Wordpress blogging engine, and the MediaWiki engine that powers Wikipedia. PHP
also powers important services like the `Ushahidi`_ platform for crowdsourced
community reporting on distributed events.

Like PHP, `Perl`_ rose to popularity on the back of Linux. Unlike PHP, which
grew specifically as a web development platform, Perl rose to prominence as
a system administrator's tool, using regular expressions to string together
and manipulate the output of text-based Linux operating system commands. When
shell, ``awk`` and ``sed`` were no longer up to handling a task, Perl was there
to take over.

Learning one of these languages isn't likely to provide any great insight into
aesthetically beautiful or conceptually elegant programming language design.
What it *is* likely to do is to provide some insight into how programming
language distribution and adoption works in practice, and how much that has to
do with fortuitous opportunities, accidents of history and lowering barriers to
adoption by working with redistributors to be made available by default, rather
than the inherent capabilities of the languages themselves.

In particular, it may provide insight into the significance of projects like
`CKAN`_, `OpenStack NFV`_, `Blender`_, `SciPy`_, `OpenMDAO`_, `PyGMO`_,
`PyCUDA`_, the `Raspberry Pi Foundation`_ and Python's adoption by a
`wide range of commercial organisations`_, for securing ongoing
institutional investment in the Python ecosystem.

.. _Lua: https://en.wikipedia.org/wiki/Lua_%28programming_language%29
.. _LuaJIT FFI: http://luajit.org/ext_ffi.html
.. _cffi: https://cffi.readthedocs.org/en/latest/#goals
.. _PHP: https://en.wikipedia.org/wiki/PHP
.. _LAMP stack: https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29
.. _Drupal: https://en.wikipedia.org/wiki/Drupal
.. _Wordpress: https://en.wikipedia.org/wiki/WordPress
.. _MediaWiki: https://en.wikipedia.org/wiki/MediaWiki
.. _Ushahidi: https://en.wikipedia.org/wiki/Ushahidi
.. _Perl: https://en.wikipedia.org/wiki/Perl
.. _CKAN: http://ckan.org/instances/#
.. _OpenStack NFV: https://wiki.openstack.org/wiki/TelcoWorkingGroup
.. _Blender: https://www.blender.org/
.. _SciPy: http://www.scipy.org/
.. _OpenMDAO: http://openmdao.org/
.. _PyGMO: http://esa.github.io/pygmo/
.. _PyCUDA: https://developer.nvidia.com/pycuda
.. _Raspberry Pi Foundation: https://www.raspberrypi.org/
.. _wide range of commercial organisations: https://us.pycon.org/2015/sponsors/


Computational thinking: Scratch, Logo
-------------------------------------

Finally, I fairly regularly get into discussions with functional and
object-oriented programming advocates claiming that those kinds of languages
are just as easy to learn as procedural ones.

I think the OOP folks have a point if we're talking about teaching through
embodied computing (e.g. robotics), where the objects being modelled in
software have direct real world counterparts the students can touch, like
sensors, motors, and relays.

For everyone else though, I now have a standard challenge: pick up a cookbook,
translate one of the recipes into the programming language you're claiming is
easy to learn, and then get a student that understands the language the
original cookbook was written in to follow the translated recipe. Most of the
time folks don't need to actually follow through on this - just running it
as a thought experiment is enough to help them realise how much prior knowledge
their claim of "it's easy to learn" is assuming. (I'd love to see academic
researchers perform this kind of study for real though - I'd be genuinely
fascinated to read the results)

Another way to tackle this problem though is to go learn the languages that
are actually being used to start teaching computational thinking to children.

One of the most popular of those is `Scratch`_, which uses a drag-and-drop
programming interface to let students manipulate a self-contained graphical
environment, with sprites moving around and reacting to events in that
environment.

This idea of using a special purpose educational language to manipulate a
graphical environment isn't new though, with one of the earliest incarnations
being the `Logo`_ environment created back in the 1960's. In Logo (and similar
environments like Python's own ``turtle`` module), the main thing you're
interacting with is a "turtle", which you can instruct to move around and
modify its environment by drawing lines. This way, concepts like command
sequences, repetition, and state (e.g. "pen up", "pen down") can be introduced
in a way that builds on people's natural intuitions ("imagine you're the turtle,
what's going to happen if you turn right 90 degrees?")

Going back and relearning one of these languages as an experienced programmer
is most useful as a tool for unlearning: the concepts they introduce help
remind us that these are concepts that we take for granted now, but needed to
learn at some point as beginners. When we do that, we're better able to work
effectively with students and other newcomers, as we're more likely to
remember to unpack our chains of logic, including the steps we'd otherwise take
for granted.

.. _Scratch: https://en.wikipedia.org/wiki/Scratch_%28programming_language%29
.. _Logo: https://en.wikipedia.org/wiki/Logo_%28programming_language%29
