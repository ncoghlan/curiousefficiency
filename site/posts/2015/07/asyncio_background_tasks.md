.. title: Background tasks in Python 3.5
.. slug: asyncio-background-calls
.. date: 2015-07-10 08:17:53 UTC
.. tags: python
.. category:
.. link: 
.. description: 
.. type: text

One of the recurring questions with asyncio is "How do I execute one or two
operations asynchronously in an otherwise synchronous application?"

Say, for example, I have the following code:

    :::pycon
    >>> import itertools, time
    >>> def ticker():
    ...     for i in itertools.count():
    ...         print(i)
    ...         time.sleep(1)
    ...
    >>> ticker()
    0
    1
    2
    3
    ^CTraceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 4, in ticker
    KeyboardInterrupt

With the native coroutine syntax coming in Python 3.5, I can change that
synchronous code into event-driven asynchronous code easily enough:

    :::python
    import asyncio, itertools
    async def ticker():
        for i in itertools.count():
            print(i)
            await asyncio.sleep(1)

But how do I arrange for that ticker to start running in the background? What's
the coroutine equivalent of appending `&` to a shell command?

It turns out it looks something like this:

    :::python
    import asyncio
    def schedule_coroutine(target, *, loop=None):
        """Schedules target coroutine in the given event loop

        If not given, *loop* defaults to the current thread's event loop

        Returns the scheduled task.
        """
        if asyncio.iscoroutine(target):
            return asyncio.ensure_future(target, loop=loop)
        raise TypeError("target must be a coroutine, "
                        "not {!r}".format(type(target)))

**Update:** *This post originally suggested a combined "run_in_background"
helper function that handle both scheduling coroutines and calling arbitrary
callables in a background thread or process. On further reflection, I decided
that was unhelpfully conflating two different concepts, so I replaced it with
separate "schedule_coroutine" and "call_in_background" helpers*

So now I can do:

    :::pycon
    >>> import itertools
    >>> async def ticker():
    ...     for i in itertools.count():
    ...         print(i)
    ...         await asyncio.sleep(1)
    ...
    >>> ticker1 = schedule_coroutine(ticker())
    >>> ticker1
    <Task pending coro=<ticker() running at <stdin>:1>>

But how do I run that for a while? The event loop won't run unless the current
thread starts it running and either stops when a particular event occurs, or
when explicitly stopped. Another helper function covers that:

    :::python
    def run_in_foreground(task, *, loop=None):
        """Runs event loop in current thread until the given task completes

        Returns the result of the task.
        For more complex conditions, combine with asyncio.wait()
        To include a timeout, combine with asyncio.wait_for()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        return loop.run_until_complete(asyncio.ensure_future(task, loop=loop))

And then I can do:

    :::pycon
    >>> run_in_foreground(asyncio.sleep(5))
    0
    1
    2
    3
    4

Here we can see the background task running while we wait for the foreground
task to complete. And if I do it again with a different timeout:

    :::pycon
    >>> run_in_foreground(asyncio.sleep(3))
    5
    6
    7

We see that the background task picked up again right where it left off
the first time.

We can also single step the event loop with a zero second sleep (the ticks
reflect the fact there was more than a second delay between running each
command):

    :::pycon
    >>> run_in_foreground(asyncio.sleep(0))
    8
    >>> run_in_foreground(asyncio.sleep(0))
    9

And start a second ticker to run concurrently with the first one:

    :::pycon
    >>> ticker2 = schedule_coroutine(ticker())
    >>> ticker2
    <Task pending coro=<ticker() running at <stdin>:1>>
    >>> run_in_foreground(asyncio.sleep(0))
    0
    10

The asynchronous tickers will happily hang around in the background, ready to
resume operation whenever I give them the opportunity. If I decide I want to
stop one of them, I can cancel the corresponding task:

    :::pycon
    >>> ticker1.cancel()
    True
    >>> run_in_foreground(asyncio.sleep(0))
    1
    >>> ticker2.cancel()
    True
    >>> run_in_foreground(asyncio.sleep(0))

But what about our original *synchronous* ticker? Can I run that as a
background task? It turns out I can, with the aid of another helper function:

    :::python
    def call_in_background(target, *, loop=None, executor=None):
        """Schedules and starts target callable as a background task

        If not given, *loop* defaults to the current thread's event loop
        If not given, *executor* defaults to the loop's default executor

        Returns the scheduled task.
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if callable(target):
            return loop.run_in_executor(executor, target)
        raise TypeError("target must be a callable, "
                        "not {!r}".format(type(target)))


However, I haven't figured out how to reliably cancel a task running in a
separate thread or process, so for demonstration purposes, we'll define a
variant of the synchronous version that stops automatically after 5 ticks
rather than ticking indefinitely:

    :::python
    import itertools, time
    def tick_5_sync():
        for i in range(5):
            print(i)
            time.sleep(1)
        print("Finishing")

The key difference between scheduling a callable in a background thread and
scheduling a coroutine in the current thread, is that the callable will start
executing immediately, rather than waiting for the current thread
to run the event loop:

    :::pycon
    >>> threaded_ticker = call_in_background(tick_5_sync); print("Starts immediately!")
    0
    Starts immediately!
    >>> 1
    2
    3
    4
    Finishing

That's both a strength (as you can run multiple blocking IO operations in
parallel), but also a significant weakness - one of the benefits of explicit
coroutines is their predictability, as you know *none* of them will start
doing anything until you start running the event loop.