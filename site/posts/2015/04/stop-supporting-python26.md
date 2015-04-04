.. title: Stop Supporting Python 2.6 (For Free)
.. slug: stop-supporting-python26
.. date: 2015-04-04 09:30:05 UTC
.. tags: python
.. category: 
.. link: 
.. description: 
.. type: text

(Note: I'm speaking with my "CPython core developer" hat on in this article,
rather than my "Red Hat employee" one, although it's the latter role that
gave me broad visibility into the Fedora/RHEL/CentOS Python ecosystem)

Alex Gaynor recently raised some
[significant concerns](https://alexgaynor.net/2015/mar/30/red-hat-open-source-community/)
in relation to his perception that Red Hat expects the upstream community
to support our long term support releases for as long as we do, only without
getting paid for it.

That's not true, so I'm going to say it explicitly: if you're currently
supporting Python 2.6 for free because folks using RHEL 6 or one of its
derivatives say they need it, and this is proving to be a hassle for you,
then stop. If they complain, then point them at this post, as providing an
easily linkable reference for that purpose is one of the main reasons I'm
writing it. If they still don't like it, then you may want to further suggest
that they come argue with me about it, and leave you alone.

The affected users have more options than they may realise, and upstream
open source developers shouldn't feel obliged to donate their own time to
help end users cope with organisations that aren't yet able to upgrade their
internal infrastructure in a more timely fashion.

Red Hat Supported Python Upgrade Paths
======================================

Since [September 2013](https://developerblog.redhat.com/2013/09/12/rhscl1-ga/),
Red Hat Enterprise Linux subscriptions have included access to an additional
component called
[Red Hat Software Collections](https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/1/html/1.2_Release_Notes/chap-RHSCL.html#sect-RHSCL-About). You can think of Software Collections roughly
as "virtualenv for the system package manager", providing access to newer
language runtimes (including Python 2.7 and 3.3), database runtimes, and
web server runtimes, all without interfering with the versions of those
integrated with (and used by) the operating system layer itself.

This model (and the fact they're included with the base Red Hat Enterprise
Linux subscription) means that Red Hat subscribers are able to install
and use these newer runtimes without needing to upgrade the entire operating
system.

Since [June 2014](https://developerblog.redhat.com/2014/06/10/red-hat-enterprise-linux-7-now-generally-available/),
Red Hat Enterprise Linux 7 has also been available, including an upgrade of
the system Python to Python 2.7. The latest release of that is
[Red Hat Enterprise Linux 7.1](https://www.redhat.com/en/about/press-releases/red-hat-continues-platform-innovation-general-availability-first-minor-release-red-hat-enterprise-linux-7).

As Red Hat subscriptions all include free upgrades to new releases, the main
barrier to deployment of these newer Python releases is
[institutional inertia](https://twitter.com/kevinrkosar/status/583786245261754368).
While it's entirely admirable that many upstream developers are generous
enough to help their end users work around this inertia, in the long run
doing so is detrimental for everyone concerned, as long term sustaining
engineering for old releases is genuinely demotivating for upstream
developers (it's a good job, but a lousy way to spend your free time), and
for end users, working around institutional inertia this way reduces the
pressure to actually get the situation addressed properly.

Beyond Red Hat Enterprise Linux, Red Hat's portfolio also includes
both the [OpenShift](https://www.openshift.com/) Platform-as-a-Service
offering and the [Feed Henry](http://www.feedhenry.com/) Mobile Application
Platform. For many organisations looking to adopt an iterative approach to
web service development, those are going to be a better fit than deploying
directly to Red Hat Enterprise Linux and building a custom web service
management system around that.

Third Party Supported Python Upgrade Paths
==========================================

The current Red Hat supported upgrade paths require administrative access to
a system. While it's aimed primarily at scientific users, the comprehensive
[Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/)
from Continuum Analytics is a good way to obtain prebuilt versions of Python
for Red Hat Enterprise Linux that can be installed by individual users
without administrative access.

At Strata 2015, Continuum's Python distribution not only featured in a
combined announcement regarding on-premise deployment of [Anaconda Cluster
together with Red Hat Storage](http://redhatstorage.redhat.com/2015/02/17/deploying-pyspark-on-red-hat-storage-glusterfs/),
but also in Microsoft's announcement of Python support in the
[Azure Machine Learning service](http://continuum.io/blog/azureml)

For users that don't need a full scientific Python distribution, Continuum
Analytics also offer [miniconda](http://continuum.io/downloads) which just
provides a Python runtime and the conda package manager, providing end users
with a cross-platform way to obtain and manage multiple Python runtimes
without needing administrative access to their systems.

Community Supported Python Upgrade Paths
========================================


The question of providing upgrade paths for folks without an active Red Hat
subscription has also been taken into consideration.

In [January 2014](https://www.redhat.com/en/about/press-releases/red-hat-and-centos-join-forces)
Red Hat became an official sponsor of the long established CentOS project,
with the aim of providing a stable base for community open source innovation
above the operating system layer (this aim contrasts with the aims of the
Fedora project, which is intended primarily to drive innovation within the
operating system layer itself).

CentOS 7 was originally released in
[July 2014](http://seven.centos.org/2014/07/release-announcement-for-centos-7x86_64/),
and the latest release, CentOS 7(1503), was just published (as the name
suggests) in
[March 2015](http://seven.centos.org/2015/03/centos-7-1503-is-released/)).

For CentOS and other RHEL derivatives, the upstream project for Red Hat
Software Collections is hosted at softwarecollections.org, making these
collections available to the whole Fedora/RHEL/CentOS ecosystem, rather than
only being available to Red Hat subscribers.

Folks running Fedora Rawhide that are particularly keen to be on the cutting
edge of Python can even obtain prerelease Python 3.5 nightly builds as a
software collection from Miro Hrončok's
[Fedora COPR repository](https://copr.fedoraproject.org/coprs/churchyard/python3-nightly/).

In addition to maintaining Fedora itself, the Fedora community also maintains
the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL)
(EPEL) repositories, providing ready access to non-conflicting packages
beyond those in the set included in the base Red Hat Enterprise Linx and
CentOS releases.

Providing Commercial Red Hat Enterprise Linux Support
=====================================================

If projects are regularly receiving requests for support on Red Hat Enterprise
Linux and derived platforms, and the developers involved are actively looking
to build a sustainable business around their software, then a steady stream
of these requests may represent an opportunity worth exploring. After all,
Red Hat's subscribers all appreciate the value that deploying commercially
supported open source software can bring to an organisation, and are
necessarily familiar with the use of software subscriptions to support
sustaining engineering and the ongoing development of new features for the
open source software that they deploy.

One of the key things that many customers are looking for is pre-release
integration testing to provide some level of assurance that the software
they deploy will work in their environment, while another is a secure
development and distribution pipeline that ensures that the software they
install is coming from organisations that they trust.

One of Red Hat's essential tools for managing this distributed integration
testing and content assurance effort is its
[Partner Program](https://www.redhat.com/en/partners). This program is
designed to not only assist Red Hat subscribers in finding supported
software that meets their needs, but also to provide Red Hat, partners, and
customers with confidence that the components of deployed solutions will
work well together in target deployment environments.

Specifically for web service developers that would like to provide a
supported on-premise offering, last year's announcement of a [Container Certification Program](https://www.redhat.com/en/about/press-releases/red-hat-announces-certification-for-containerized-applications-extends-customer-confidence-and-trust-to-the-cloud)
(with Red Hat Enterprise Linux 7 and the OpenShift Platform-as-a-Service
offering as certified container hosts) extended Red Hat's certification
programs to cover the certification of Docker containers in addition to
other forms of Linux application deployment.

Even more recently, the
[Red Hat Container Development Kit](http://connect.redhat.com/zones/containers)
was introduced to help streamline that certification process for Red Hat
Independent Software Vendor Partners.

But these are all things that folks should only explore if they're
specifically interested in building a commercial support business around
their software. If users are trying to get long term maintenance support
for a community project for free, then upstream developers should be sending
a single unified message in response: don't assume you'll be able to run
new versions of open source software on old platforms unless you're
specifically paying someone to ensure that happens.

I'm not saying this because I work for a platform vendor that gets paid (at
least in part) to do this, I'm saying it because most open source projects
are maintained by innovators that are upgrading their technology stacks
regularly, where versions of components are already old after 2 years and
truly ancient after 5. Expecting open source innovators to provide long term
maintenance for free is simply unreasonable - regularly upgrading their own
stacks means they don't need this long term platform support for themselves,
so the folks that are seeking it should be expected to pay for it to happen.
(Apparent exceptions like CentOS aren't exceptions at all: sustaining
engineering on CentOS is instead a beneficial community byproduct of the
[paid sustaining engineering](http://crunchtools.com/deep-dive-rebase-vs-backport/)
that goes into Red Hat Enterprise Linux).
