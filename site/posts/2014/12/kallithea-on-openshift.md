.. title: Running Kallithea on OpenShift
.. slug: kallithea-on-openshift
.. date: 2014-12-11 03:18:26 UTC
.. tags: python,kallithea,docker,openshift
.. link: 
.. description: 
.. type: text

Kallithea for CPython
=====================

The CPython core development team are currently evaluating our options for
modernising our core development workflows to better match the standards
set by other projects and services like OpenStack and GitHub.

The first step in [my own proposal](https://www.python.org/dev/peps/pep-0474/)
for that is to migrate a number of the support repositories currently hosted
using a basic Mercurial server on hg.python.org to an instance of
[Kallithea](https://kallithea-scm.org/) hosted as forge.python.org.
(Kallithea is a GPLv3 Python project that was forked from RhodeCode after
certain aspects of the latter's commercialisation efforts started alienating
several members of their user and developer community)

Tymoteusz Jankowski (a contributor to Allegro Group's open source data centre
inventory management system, [Ralph](http://ralph.allegrogroup.com/)), has
already started looking at the steps that might be involved in integrating a
Kallithea instance into the PSF's Salt based
[infrastructure automation](https://github.com/xliiv/psf-salt/tree/kallithea).

However, for my proposal to be as successful as I would like it to be, I need
the barriers to entry for the development and deployment of the upstream
Kallithea project itself to be as low as possible. One of the challenges
we've often had with gaining contributors to CPython infrastructure
maintenance is the relatively high barriers to entry for trying out service
changes and sharing them with others, so this time I plan to tackle that
concern *first*, by ensuring that addressing it is a mandatory requirement
in my proposal.

That means tackling two particular problems:

* Having a way to easily run local test instances for development and
  experimentation
* Having a way to easily share demonstration instances with others

For the first problem, I plan to rely on Vagrant and Docker, while for the
second I'll be relying on the free tier in Red Hat's OpenShift Online
service. Unfortunately, while the
[next generation](http://www.openshift.org/) of OpenShift will support Docker
images natively, for the time being, I need to tackle these as two separate
problems, as there aren't any existing Docker based services I'm aware of
with a free tier that is similarly suited to the task of sharing development
prototypes for open source web services with a broad audience (let alone
any such services that are also
[fully open source](https://github.com/openshift)).

Once I have these working to my satisfaction, I'll propose them to the
Kallithea team for inclusion in the Kallithea developer documentation, but
in the meantime I'll just document them here on the blog.

Enabling Kallithea deployment on OpenShift
==========================================

My first priority is to get a public demonstration instance up and running
that I can start tweaking towards the CPython core development community's
needs (e.g. installing the custom repo hooks we run on hg.python.org), so
I'm starting by figuring out the OpenShift setup needed to run public
instances - the Vagrant/Docker based setup for local development will come
later.

Conveniently, WorldLine previously created an [OpenShift quickstart for
RhodeCode](https://github.com/worldline/openshift-rhodecode) and published
it under the Apache License 2.0, so I was able to use that as a starting
point for my own
[Kallithea quickstart](https://github.com/ncoghlan/openshift-kallithea).

While I personally prefer to run Python web services under mod_wsgi in order
to take advantage of Apache's authentication & authorisation plugin ecosystem,
that's not a significant concern for the demonstration server use case I have
in mind here. There are also some other aspects in the WorldLine quickstart
I'd like to understand better and potentially change (like figuring out a
better way of installing git that doesn't involve hardcoding a particular
version), but again, not a big deal for demonstration instances - rather
than worrying about them too much, I just annotated them as `TODO` comments
in the OpenShift hook source code.

I'd also prefer to be running under the official Python 2.7 cartridge rather
than a DIY cartridge, but again, my focus at this point is on getting
something up and running, and then iterating from there to improve it.

That meant adapting the quickstart from RhodeCode to Kallithea was mostly
just a matter of changing the names of the various components being installed
and invoked, together with changing the actual installation and upgrade steps
to be based on Kallithea's deployment instructions.

The keys to this are the
[build hook](https://github.com/ncoghlan/openshift-kallithea/blob/master/.openshift/action_hooks/build)
and the
[start hook](https://github.com/ncoghlan/openshift-kallithea/blob/master/.openshift/action_hooks/start).
The [OpenShift docs](https://developers.openshift.com/en/managing-action-hooks.html)
have more details on the various available action hooks and when they're run.

In addition to the `TODO` comments noted above, I also added various comments
explaining *what* different parts of the action hook scripts were doing.

(Note: I haven't actually *tested* an upgrade, only the initial
deployment described below, so I can't be sure I have actually adapted the
upgrade handling correctly yet)

Deploying my own Kallithea instance
===================================

I already have an OpenShift account, so I could
[skip that step](https://www.openshift.com/app/account/new), and just
create a new app under my existing account. However, I didn't have the command
line tools installed, so that was the first step in creating my own instance:

    sudo yum install /usr/bin/rhc

yum is able to figure out on my behalf that it is `rubygems-rhc` that
provides the command line tools for OpenShift in Fedora (alternatively,
I could have looked that up myself in the
[OpenShift client tools installation docs](https://developers.openshift.com/en/getting-started-client-tools.html#fedora)).

The next step was to configure the command line tools to use my OpenShift
Online account, generate a local login token for this machine, and upload
my public SSH key to OpenShift Online. That process involved working through
the interactive prompts in:

    rhc setup

With those preliminary OpenShift steps out of the way, it was time to
move on to deploying the application itself. It's worth noting that
app creation automatically clones a local git repo named after the application,
so I created a separate "app_repos" subdirectory in my development directory
specifically so I could call my OpenShift app "kallithea" without conflicting
with my local clone of the main kallithea repo.

As described in the quickstart README, the app creation command is:

    rhc app create kallithea diy-0.1 postgresql-9.2

That churned away for a while, and then attempted to clone the app repo
locally over ssh (with SSH putting up a prompt to accept the validity of the
app's freshly generated SSH key). I'm not sure why, but for some reason that
automatic clone operation didn't work for me. `rhc` put up a detailed
message explaining that the app creation had worked, but the clone step had
failed. Fortunately, as the troubleshooting notice suggested, a subsequent
`rhc git-clone kallithea` worked as expected.

OpenShift provides a default app skeleton automatically, but I actually
want to get rid of that and replace it with the contents of the quickstart
repo:

    rm -R diy .openshift misc README.md
    git add .
    git commit -m "Remove template files"
    git remote add quickstart -m master https://github.com/ncoghlan/openshift-kallithea.git
    git pull -s recursive -X theirs quickstart master

The default merge commit message that popped up was fine, so I just accepted
that and moved on to the most interesting step:

    git push

Because this is the first build, there's a lot of output related to
installing and building the PostgreSQL driver and git, before moving on
to installing Kallithea and its dependencies.

However, that still didn't take long, and completed without errors, so I now
have my own Kallithea instance
[up and running](http://kallithea-ncoghlan.rhcloud.com/).

And no, the default admin credentials created by the quickstart won't work
anymore - I immediately logged in to the admin account to change them!

Where to from here?
===================

There are various aspects of the current quickstart that are far from ideal,
but I don't plan to spend a lot of time worrying about it when I know that
support for using Docker images directly in OpenShift is coming at some
point in the not too distant future.

One of the key advantages of Docker is the much nicer approach it offers to
layered application development where infrastructure experts can provide
base images for others to build on, and in the case of deploying Python
applications with mod_wsgi, that means listening to Graham Dumpleton (the
author of mod_wsgi, currently working for New Relic).

On that front, Graham has actually been
[working on](http://blog.dscpl.com.au/2014/12/hosting-python-wsgi-applications-using.html)
creating a set of Debian based
[mod_wsgi Docker images](https://registry.hub.docker.com/u/grahamdumpleton/mod-wsgi-docker/)
that Python developers can use, rather than having to build their own from
scratch.

In my case, I'd really prefer something based on CentOS 7 or Fedora Cloud,
but that's a relatively minor quibble, and Graham's images should still make
a great basis for putting together a Vagrant+Docker based local workflow
for folks working on Kallithea.

That, however, is a topic for a future post :)
