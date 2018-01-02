About Curious Efficiency
========================

About the site
--------------

Curious Efficiency is the intermittently updated personal website of Nicholas
Coghlan, CPython core developer, PSF Fellow, software development toolsmith,
cognitive science dabbler, and cynical idealist.

The main portion of the site is generated via
`Nikola <http://getnikola.com/>`__,
hosted on `GitHub Pages <https://pages.github.com/>`__,
and under source control on
`BitBucket <https://bitbucket.org/ncoghlan/curiousefficiency/>`__.

Python specific technical writing tends to end up on the
`ReadTheDocs <http://readthedocs.org/>`__ powered
`Python Notes <http://python-notes.curiousefficiency.org>`__ subsite.


About the name
--------------

Curious Efficiency is actually a reframing of my original blog title,
Boredom & Laziness - the original boredomandlaziness.org URLs now redirect
here. The original site blurb on Boredom & Laziness read as follows:

   There are a couple of very, very scary things in this world.

   The first is a bored human. Bored humans have time to indulge their
   curiosity, with potentially amazing results.

   The second is a lazy human. Lazy humans can be quite inventive when it
   comes to figuring out how to do less work.

   So, here's to boredom & laziness - two of the prime movers in human progress!

"Curious Efficiency" is really just a nicer way of referring to the same
concept.

`This post <../posts/2012/07/the-title-of-this-blog.html>`__ goes into some
additional detail on the concepts that inspired the naming, both the original
form, and the current more conventionally acceptable phrasing.


About the author
----------------

.. image:: ../files/pycon2011_language_summit_cropped.jpg
   :align: right

Nick is a CPython core developer, a Fellow of the Python Software Foundation,
and the founder of the PyCon Australia Education Seminar.

He is the author or co-author of several accepted Python Enhancement Proposals
(including PEP 453, which saw the ``pip`` installer bundled with Python 3.4+,
PEP 466, which saw several key Python 3 network security enhancements backported
to the Python 2.7 series, and PEP 538, which updated CPython to coerce the
legacy ASCII-based C locale to a suitable UTF-8 based locale when one is
available), and has also accepted a number of PEPs on Guido van Rossum's behalf
as BDFL-Delegate.

Nick is currently the BDFL-Delegate for most packaging related PEPs, serving
as the primary liaison between the CPython core development team and the
`Python Packaging Authority <https://www.pypa.io/>`__. His own efforts in the
packaging space are focused primarily on the
`Python Packaging User Guide <https://packaging.python.org>`_, and the
`pipenv <https://packaging.python.org/tutorials/managing-dependencies/>`_
application dependency management project.

At the PyCon US 2013 language summit, Nick successfully argued for updates to
the Python Enhancement Proposal process (described in PEP 1) that allowed
BDFL-Delegates to approve PEPs that don't affect the language definition or
the standard library directly on the relevant mailing lists (without needing
to rehash the discussions on python-dev).

In addition to CPython, the PSF, the PyPA, and the PSF's
`Packaging Working Group <https://wiki.python.org/psf/PackagingWG>`__,
other projects & programs of particular current interest include:

* `Kubernetes <https://kubernetes.io/>`__: a Google created open source
  application deployment platform, designed to ease adoption for folks
  accustomed to managing their own Linux servers directly, and supported across
  all major public clouds. I'm interested in this as I believe it addresses many
  of the vendor lock-in concerns otherwise raised against public cloud adoption
  (and unlike previous efforts in that space, it has support from the major
  public cloud vendors themselves).
* `OpenShift <https://www.openshift.org/>`__: Red Hat's fully open source
  Kubernetes-based Platform-as-a-Service offering that provides tools to
  handle automatic updates of deployed images when either application code
  or the underlying base image changes. I'm interested in this as Red Hat are
  veterans at selling to the legacy infrastructure crowd, and many of the "But
  what about..." objections raised against plain Kubernetes already have
  solutions built in to OpenShift.
* `Zappa <https://www.zappa.io/>`__: a toolkit for running Python WSGI
  applications in AWS Lambda behind AWS API Gateway. I'm interested in this
  as I think it's the level of "Don't bother me with irrelevant infrastructure
  details" that Kubernetes et al should be aspiring to, but they're not there
  yet.
* `Software Collections <https://www.softwarecollections.org/en/>`__: a
  Red Hat supported approach to deploying platform components (such as language
  runtimes, database engines and web servers) on Linux, such that end user
  applications can use newer versions without interfering with the versions
  integrated directly into the underlying operating system distribution. I'm
  interested in this as "We have to use the system Python in some ancient RHEL
  version and aren't allowed to install packages from PyPI" is one of the
  largest drags on innovation in the Python ecosystem, and Software
  Collections are the main mechanism that Red Hat uses to offer newer Python
  runtimes to their customers.
* `Zappa <https://www.zappa.io/>`__: a toolkit for running Python WSGI
  applications in AWS Lambda behind AWS API Gateway. I'm interested in this
  as I think it's the level of "Don't bother me with irrelevant infrastructure
  details" that Kubernetes et al should be aspiring to, but they're not there
  yet.
* `Conda <https://conda.io/docs/>`__: a cross-platform environment manager
  created initially for the Python data science community. Its language
  independent design means it can not only manage the installation of Python
  packages, but also manage the Python runtime itself, external binary
  dependencies written in C/C++/FORTRAN/etc, and data analysis components
  written in other languages entirely (such as R and Julia).
* `Fedora Scientific <https://labs.fedoraproject.org/en/scientific/>`__: a
  KDE-based Fedora desktop distribution with a range of science and data
  analysis applications pre-installed, including IPython Notebook.


Selected articles, presentations and interviews
-----------------------------------------------

Selected Python Enhancement Proposals:

* PEP 338: `Executing modules as scripts <https://www.python.org/dev/peps/pep-0338/>`__ (aka "the -m switch")
* PEP 343: `The "with" statement <https://www.python.org/dev/peps/pep-0343/>`__ (co-authored with Guido van Rossum)
* PEP 366: `Main module explicit relative imports <https://www.python.org/dev/peps/pep-0366/>`__
* PEP 394: `The "python" command on UNIX-like systems <https://www.python.org/dev/peps/pep-0394/>`__ (co-authored with Kerrick Staley)
* PEP 414: `Explicit Unicode Literal for Python 3.3 <https://www.python.org/dev/peps/pep-0414/>`__ (co-authored with Armin Ronacher)
* PEP 432 (Draft): `Simplifying the CPython interpreter startup sequence <https://www.python.org/dev/peps/pep-0432/>`__
* PEP 453: `Bootstrapping pip in Python installations <https://www.python.org/dev/peps/pep-0453/>`__ (co-authored with Donald Stufft)
* PEP 466: `Network Security Enhancements for Python 2.7.x <https://www.python.org/dev/peps/pep-0466/>`__
* PEP 477: `Backport ensurepip to Python 2.7 <https://www.python.org/dev/peps/pep-0477/>`__ (co-authored with Donald Stufft)
* PEP 489: `Multi-phase extension module initialisation <https://www.python.org/dev/peps/pep-0489/>`__ (co-authored with Petr Viktorin and Stefan Behnel)
* PEP 493: `HTTPS verification migration tools for Python 2.7 <https://www.python.org/dev/peps/pep-0493/>`__ (co-authored with Robert Kuska and Marc-Andre Lemburg)
* PEP 538: `Coercing the legacy C locale to a UTF-8 based locale <https://www.python.org/dev/peps/pep-0538/>`__
* PEP 565: `Show DeprecationWarning in __main__ <https://www.python.org/dev/peps/pep-0565/>`__
* PEP 558 (Draft): `Defined semantics for locals() <https://www.python.org/dev/peps/pep-0558/>`__

Selected Python related presentations (video links):

* Opportunities & Challenges in Open Collaboration

  * `PyCon Pune 2017 <http://pyvideo.org/pycon-pune-2017/keynote-opportunities-and-challenges-in-open-collaboration.html>`__

* Contributors, Colleagues, Clients & Customers: Sustaining Open Source Communities

  * `PyGotham 2015 keynote <http://pyvideo.org/pygotham-2015/contributors-colleagues-clients-customers-su.html>`__
  * `PyCon Poland 2015 keynote <http://pyvideo.org/pycon-pl-2015/contributors-colleagues-clients-customers-sustaining-open-source-communities.html>`__

* Python Beyond (C)Python (Adventures in Software Distribution):

  * `PyCon New Zealand 2014 keynote <http://pyvideo.org/video/3211/nick-coghlan-python-beyond-cpython-keynote>`__
  * `SciPy 2014 keynote <http://pyvideo.org/video/2785/python-beyond-cpython-adventures-in-software-dis>`__

* Python Packaging:

  * `Python Packaging 2.0: Playing Well With Others <https://www.youtube.com/watch?v=7An2GobbSWU>`__ (linux.conf.au 2014)
  * `Nobody Expects the Python Packaging Authority <http://pyvideo.org/video/2197/nobody-expects-the-python-packaging-authority>`__ (PyCon Australia 2013)

* CPython Core Development:

  * `Here be dragons: some elegant & ugly hacks in CPython <https://www.youtube.com/watch?v=VIBmWnlDjXc>`__ (PyCon Australia 2014)
  * `How Python Evolves <http://pyvideo.org/video/997/how-python-evolves-and-how-you-can-help-make-it>`__ (PyCon Australia 2011)

Selected Python related articles and presentation reviews:

* `Considering Python's target audience <https://www.curiousefficiency.org/posts/2017/10/considering-pythons-target-audience.html>`__
* `The Python Packaging Ecosystem (September 2016) <https://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html>`__
* `27 Languages to Improve Your Python <https://www.curiousefficiency.org/posts/2015/10/languages-to-improve-your-python.html#broadening-our-horizons>`__
* `The Transition to Multilingual Programming <https://developerblog.redhat.com/2014/09/09/transition-to-multilingual-programming-python/>`__
* `Why Python 4.0 won't be like Python 3.0 <https://developerblog.redhat.com/2014/09/17/why-python-4-0-wont-be-like-python-3-0/>`__
* `Python 3 Q & A <http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html>`__
* `Linux Weekly News article <http://lwn.net/Articles/580399/>`__ on my Python Packaging 2.0 presentation at linux.conf.au 2014
* `Justifying Python language changes <https://www.curiousefficiency.org/posts/2011/02/justifying-python-language-changes.html>`__

Selected software design, development and deployment related presentations and articles:

* `Front-end Integration Testing with Splinter <http://pyvideo.org/pycon-au-2017/front-end-integration-testing-with-splinter.html>`__ (PyCon Australia 2017)
* `Tracking package updates with release-monitoring.org <https://lwn.net/Articles/711906/>` (LWN article on my linux.conf.au 2017 presentation)
* `What problem does it solve? <https://www.curiousefficiency.org/posts/2016/08/what-problem-does-it-solve.html>` (on constructively criticising API designs)
* `Musings on the culture of python-dev <http://www.curiousefficiency.org/posts/2011/04/musings-on-culture-of-python-dev.html>`__
* `Status quo wins a stalemate <http://www.curiousefficiency.org/posts/2011/02/status-quo-wins-stalemate.html>`__
* `Scripting Languages and Suitable Complexity <http://www.curiousefficiency.org/posts/2011/08/scripting-languages-and-suitable.html>`__
* `Path Dependent Development <http://pyvideo.org/video/1625/path-dependent-development-why-on-earth-are-you>`__ (PyCon Australia 2012)
* `Full Stack Integration Testing with Beaker <https://www.youtube.com/watch?v=tjUjdBm-Mqw>`__ (linux.conf.au 2014)

Selected community management related articles and interviews:

* `27 Languages to Improve Your Python (introduction) <https://www.curiousefficiency.org/posts/2015/10/languages-to-improve-your-python.html>`__
* `The Quid Pro Quo of Open Infrastructure <https://community.redhat.com/blog/2015/02/the-quid-pro-quo-of-open-infrastructure/>`__
* `Abusing Contributors is not OK <http://www.curiousefficiency.org/posts/2015/01/abuse-is-not-ok.html>`__ (reflecting on some comments from Linus Torvalds during his plenary session at linux.conf.au 2015)
* `Effective communication, brain hacking and diversity <http://www.curiousefficiency.org/posts/2011/07/effective-communication-brain-hacking.html>`__
* `opensource.com interview <http://opensource.com/business/14/7/new-membership-process-python-software-foundation>`__ on my joining the PSF board of directors

Podcast appearances (in reverse chronological order):

* `Free as in Freedom <http://faif.us/cast/2015/mar/03/0x55/>`__ (with hosts Karen Sandler & Bradley M. Kuhn, recorded January 2015)
* `Pragmatic <http://techdistortion.com/podcasts/pragmatic/episode-35-written-by-kernel-hackers-for-kernel-hackers>`__ (with host John Chidgey, recorded August 2014)
* `From Python Import Podcast <http://frompythonimportpodcast.com/2014/03/31/episode-017-the-one-about-python-3/>`__ (with hosts Mike Pirnat & Dave Noyes and fellow guest Alex Gaynor, recorded March 2014)

  * Historical note of potential interest: I consider this discussion between Alex and myself to be one of the key events on the road to PEP 466's backport of Python 3 network security features to the Python 2.7 series, and PEP 476's switch to verifying HTTPS certificates by default in Python 2.7.9+ and 3.4.3+

* `Radio Free Python <http://radiofreepython.com/episodes/6/>`__ (with host Larry Hastings, recorded February 2012)
