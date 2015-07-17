About Curious Efficiency
========================

About the site
--------------

Curious Efficiency is the intermittently updated personal website of Nicholas
Coghlan, CPython core developer, PSF Director, Red Hat toolsmith, cognitive
science dabbler, and cynical idealist.

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

Nick is a CPython core developer and a member of the Board of Directors
for the Python Software Foundation. He is the author or co-author of several
accepted Python Enhancement Proposals (including PEP 453, which saw
the ``pip`` installer bundled with Python 3.4+, and PEP 466, which saw several
key Python 3 network security enhancements backported to the Python 2.7
series), and has also accepted a number of PEPs on Guido van Rossum's behalf
as BDFL-Delegate.

Nick is currently the BDFL-Delegate for most packaging related PEPs, serving
as the primary liaison between the CPython core development team and the
Python Packaging Authority. His own efforts in the packaging space are
focused primarily on the metadata 2.0 interoperability standards (PEP 426,
440, 459) and on aligning the ongoing work of the Python Packaging
Authority with the efforts of the Fedora Environments & Stacks working group.

At the PyCon US 2013 language summit, Nick successfully argued for updates to
the Python Enhancement Proposal process (described in PEP 1) that allowed
BDFL-Delegates to approve PEPs that don't affect the language definition or
the standard library directly on the relevant mailing lists (without needing
to rehash the discussions on python-dev).

Since June 2011, after more than 12 years in the aerospace and defence
sector with Boeing Australia, Nick has been working on development and test
infrastructure for Red Hat.

He is currently a software development workflow designer & process architect
working on Fedora's software management processes and tooling on behalf of Red
Hat's Developer Experience group.

In addition to CPython, the PSF, the
`Python Packaging Authority <https://www.pypa.io/>`__, and the
`Fedora Environments & Stacks <https://fedoraproject.org/wiki/Env_and_Stacks>`__
Working Group, other projects & programs of particular current interest include:

* `Kallithea <https://kallithea-scm.org/>`__: the Python-based fully open
  source repository management service for git and Mercurial that Nick is
  proposing to deploy as forge.python.org for use in CPython development
  `PEP 474 <https://www.python.org/dev/peps/pep-0474/>`__
* `Software Collections <https://www.softwarecollections.org/en/>`__: an
  approach to deploying platform components (such as language runtimes,
  database engines and web servers) on Linux, such that end user
  applications can use newer versions without interfering with the versions
  integrated directly into the underlying operating system distribution
* `Project Atomic <https://www.projectatomic.io/>`__: the overall integration
  project for container technology in the Fedora/RHEL/CentOS ecosystem,
  bringing Docker containers together with various other components of that
  ecosystem (most notably RPM for subcomponent packaging and rpm-ostree for
  atomic host updates)
* `Nulecule <https://github.com/projectatomic/nulecule>`__: a JSON-based
  specification for defining multi-part container based applications and
  deploying them to a range of target environments.
* `Sandboxed Applications for GNOME
  <https://wiki.gnome.org/Projects/SandboxedApps>`__: application of Linux
  container technology, kdbus and Wayland to the task of sandboxing
  desktop GUI applications.
* `Fedora Server Roles
  <https://sgallagh.wordpress.com/2014/12/11/rolekit-or-how-i-learned-to-stop-thinking-in-terms-of-packages/>`__:
  application of Linux container technology (including Nulecule) to the
  management of stateful Linux servers (e.g. domain controllers, database
  servers, file servers, backup servers, groupware servers)
* `Fedora Scientific <https://labs.fedoraproject.org/en/scientific/>`__: a
  KDE-based Fedora desktop distribution with a range of science and data
  analysis applications pre-installed, including IPython Notebook.
* `CentOS Public CI <https://wiki.centos.org/QaWiki/CI>`__: a Jenkins based
  public CI service offered by the CentOS project that (when fully
  operational) is intended to provide a common location for infrastructure
  management focused open source projects to run their integration tests
* `OpenShift <http://www.openshift.org/>`__: Red Hat's fully open source
  Platform-as-a-Service offering, with several key runtime elements of its
  next generation architecture currently being collaboratively developed with
  Google and other organisations in the upstream
  `Kubernetes <http://kubernetes.io/>`__ project
* `Red Hat Container Certification
  <http://connect.redhat.com/zones/containers/why-certify-containers>`__: a
  program that allows Red Hat subscribers to take advantage of Linux
  container technology to streamline the delivery and deployment of software
  from Red Hat Certified ISV partners


Selected articles, presentations and interviews
-----------------------------------------------

Python Enhancement Proposals:

* PEP 338: `Executing modules as scripts <https://www.python.org/dev/peps/pep-0338/>`__ (aka "the -m switch")
* PEP 394: `The "python" command on UNIX-like systems <https://www.python.org/dev/peps/pep-0394/>`__ (co-authored with Kerrick Staley)
* PEP 414: `Explicit Unicode Literal for Python 3.3 <https://www.python.org/dev/peps/pep-0414/>`__ (co-authored with Armin Ronacher)
* PEP 453: `Bootstrapping pip in Python installations <https://www.python.org/dev/peps/pep-0453/>`__ (co-authored with Donald Stufft)
* PEP 466: `Network Security Enhancements for Python 2.7.x <https://www.python.org/dev/peps/pep-0466/>`__
* PEP 426 (Draft): `Metadata for Python Software Packages 2.0 <https://www.python.org/dev/peps/pep-0426/>`__ (co-authored with Donald Stufft & Daniel Holth)
* PEP 432 (Draft): `Simplifying the CPython interpreter startup sequence <https://www.python.org/dev/peps/pep-0432/>`__
* PEP 474 (Draft): `Creating forge.python.org <https://www.python.org/dev/peps/pep-0474/>`__

Python related presentations (video links):

* Python Beyond (C)Python (Adventures in Software Distribution):

  * `PyCon New Zealand 2014 keynote <http://pyvideo.org/video/3211/nick-coghlan-python-beyond-cpython-keynote>`__
  * `SciPy 2014 keynote <http://pyvideo.org/video/2785/python-beyond-cpython-adventures-in-software-dis>`__

* Python Packaging:

  * `Python Packaging 2.0: Playing Well With Others <https://www.youtube.com/watch?v=7An2GobbSWU>`__ (linux.conf.au 2014)
  * `Nobody Expects the Python Packaging Authority <http://pyvideo.org/video/2197/nobody-expects-the-python-packaging-authority>`__ (PyCon Australia 2013)

* CPython Core Development:

  * `Here be dragons: some elegant & ugly hacks in CPython <https://www.youtube.com/watch?v=VIBmWnlDjXc>`__ (PyCon Australia 2014)
  * `How Python Evolves <http://pyvideo.org/video/997/how-python-evolves-and-how-you-can-help-make-it>`__ (PyCon Australia 2011)

Python related articles and presentation reviews:

* `The Transition to Multilingual Programming <https://developerblog.redhat.com/2014/09/09/transition-to-multilingual-programming-python/>`__
* `Why Python 4.0 won't be like Python 3.0 <https://developerblog.redhat.com/2014/09/17/why-python-4-0-wont-be-like-python-3-0/>`__
* `Python 3 Q & A <http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html>`__
* `Linux Weekly News article <http://lwn.net/Articles/580399/>`__ on my Python Packaging 2.0 presentation at linux.conf.au 2014

Software design, development and deployment related presentations and articles:

* `The Quid Pro Quo of Open Infrastructure <https://community.redhat.com/blog/2015/02/the-quid-pro-quo-of-open-infrastructure/>`__
* `Musings on the culture of python-dev <http://www.curiousefficiency.org/posts/2011/04/musings-on-culture-of-python-dev.html>`__
* `Status quo wins a stalemate <http://www.curiousefficiency.org/posts/2011/02/status-quo-wins-stalemate.html>`__
* `Scripting Languages and Suitable Complexity <http://www.curiousefficiency.org/posts/2011/08/scripting-languages-and-suitable.html>`__
* `Path Dependent Development <http://pyvideo.org/video/1625/path-dependent-development-why-on-earth-are-you>`__ (PyCon Australia 2012)
* `Full Stack Integration Testing with Beaker <https://www.youtube.com/watch?v=tjUjdBm-Mqw>`__ (linux.conf.au 2014)

Community management related articles and interviews:

* `Abusing Contributors is not OK <http://www.curiousefficiency.org/posts/2015/01/abuse-is-not-ok.html>`__ (reflecting on some comments from Linus Torvalds during his plenary session at linux.conf.au 2015)
* `Effective communication, brain hacking and diversity <http://www.curiousefficiency.org/posts/2011/07/effective-communication-brain-hacking.html>`__
* `opensource.com interview <http://opensource.com/business/14/7/new-membership-process-python-software-foundation>`__ on my joining the PSF board of directors

Podcast appearances (in reverse chronological order):

* `Free as in Freedom <http://faif.us/cast/2015/mar/03/0x55/>`__ (with hosts Karen Sandler & Bradley M. Kuhn, recorded January 2015)
* `Pragmatic <http://techdistortion.com/podcasts/pragmatic/episode-35-written-by-kernel-hackers-for-kernel-hackers>`__ (with host John Chidgey, recorded August 2014)
* `From Python Import Podcast <http://frompythonimportpodcast.com/2014/03/31/episode-017-the-one-about-python-3/>`__ (with hosts Mike Pirnat & Dave Noyes and fellow guest Alex Gaynor, recorded March 2014)

  * Historical note of potential interest: I consider this discussion between Alex and myself to be one of the key events on the road to PEP 466's backport of Python 3 network security features to the Python 2.7 series, and PEP 476's switch to verifying HTTPS certificates by default in Python 2.7.9+ and 3.4.3+

* `Radio Free Python <http://radiofreepython.com/episodes/6/>`__ (with host Larry Hastings, recorded February 2012)
