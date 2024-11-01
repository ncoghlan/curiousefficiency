title: The origin of venvstacks
slug: the-origin-of-venvstacks
date: 2024-11-01 04:21:50 UTC
tags: python
category: python
description: The story behind the creation of the "venvstacks" packaging utility
type: text

There has been a longstanding gap in the Python packaging ecosystem that has
somewhat annoyed me,
but not enough to do anything about it:
we haven't really had a good way to compose *multiple* layers of Python
virtual environments together,
allowing large dependencies (like AI and machine learning libraries)
to be shared across multiple different application environments without having
to install them directly into the base runtime environment.

Utilities for collecting up an entire Python runtime, an application, and all its
dependencies into a single deployable artifact have existed since before the turn
of the century.

We've had standardised [virtual environments](https://docs.python.org/3/library/venv.html)
(allowing multiple applications to share a base Python runtime and its directly
installed third party packages) for almost as long.

We've had [zip applications](https://docs.python.org/3/library/zipapp.html)
for a long time as well (and other utilities which build on that feature).

We've had tools like [`wagon`](https://github.com/cloudify-cosmo/wagon)
which allow us to ship a bundle of prebuilt Python wheel archives and
install them on a destination system without needing to download
anything else from the internet at installation time.

We've had tools like [`conda`](https://docs.conda.io/)
(and more recently [`uv`](https://docs.astral.sh/uv/)),
which make intelligent use of hard links on local systems to avoid
making duplicate copies of completely identical versions of packages.

We've technically had platform specific mechanisms like Linux container images,
where the contents of an environment can be built up across multiple
container image layers, with the lower layers being shared across multiple
image definitions, but have lacked a convenient way to handle the dependency
management complications involved in using these tools to share large Python
libraries.

But we've never had something which specifically took full advantage of the way
Python's import system works to enable robust structural decomposition of Python
applications into independently updatable subcomponents (with a granularity
larger than single packages).

All of this history meant that I was thoroughly intrigued when a mutual
acquaintance introduced me to the creators of the [LM Studio](https://lmstudio.ai/)
personal AI desktop application to discuss a Python packaging problem they
had looming on their technical road map: it was clear from user demand and the
rate of evolution in the Python AI/ML ecosystem that they needed a way to ship
Python AI/ML components directly to their users *without* having to wait for
those capabilities to be made available through native interfaces in other
languages (such as Swift, C++, or JavaScript), but it didn't seem obvious to them
*how* they could readily integrate that capability into LM Studio without
making the application installation process substantially more complicated
for their users.

What started as a consulting contract for a technical proof of concept,
and has since turned into a permanent position with the organisation,
proved fruitful,
and the result is the [recently published](https://lmstudio.ai/blog/venvstacks)
open source [`venvstacks`](https://pypi.org/project/venvstacks/) utility,
which is specifically designed to enable the kind of portable deterministic
artifact publishing setup that LM Studio needed, including:

* Base runtime layers
  (based on [`python-build-standalone`](https://github.com/indygreg/python-build-standalone))
* Framework layers (for shipping large dependencies, such as Apple MLX or PyTorch)
* Application layers (including additional unpackaged "launch modules" for app execution)

There are certainly still some technical limitations to be addressed (the
[dynamic linking problem](https://github.com/lmstudio-ai/venvstacks/issues/38)
with layering virtual environments like this is notorious amongst Python packaging
experts for a reason), but even in its current form, `venvstacks` is already capable
enough to power the recent inclusion of
[Apple MLX support](https://lmstudio.ai/blog/lmstudio-v0.3.4#mlx-in-lm-studio-using-python)
in LM Studio.
