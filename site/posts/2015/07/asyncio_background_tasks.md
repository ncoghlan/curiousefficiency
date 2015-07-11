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
    async def ticker():
        for i in itertools.count():
            print(i)
            await asyncio.sleep(1)

But how do I kick that ticker off as a background task? What's the Python
REPL's equivalent of appending `&` to a shell command?

It turns out it looks something like this:

    :::python
    import asyncio
    def run_in_background(target, *, loop=None):
        """Schedules target as a background task

        Returns the scheduled task.

        If target is a future or coroutine, equivalent to asyncio.ensure_future
        If target is a callable, it is scheduled in the default executor
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        try:
            return asyncio.ensure_future(target, loop=loop)
        except TypeError:
            pass
        if callable(target):
            return loop.run_in_executor(None, target)
        raise TypeError("background task must be future, coroutine or "
                        "callable, not {!r}".format(type(target)))

So now I can do:

    :::pycon
    >>> async def ticker():
    ...     for i in itertools.count():
    ...         print(i)
    ...         await asyncio.sleep(1)
    ...
    >>> ticker1 = run_in_background(ticker())
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
        return loop.run_until_complete(asyncio.ensure_future(task))

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
    >>> ticker2 = run_in_background(ticker())
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
background task? It turns out I can, as that's the reason for the special
handling of callables in `run_in_background`. However, I haven't figured out
how to reliably cancel a task created through `run_in_executor` so we'll make
sure this variant of the synchronous version stops on its own:

    :::python
    import itertools, time
    def ticker_sync(stop):
        for i in range(stop):
            print(i)
            time.sleep(1)
        print("Finishing")

The key difference between scheduling a callable and a coroutine, is that the
callable will start executing immediately in another thread, rather than
waiting for the current thread to run the event loop:

    :::pycon
    >>> threaded_ticker = run_in_background(lambda: ticker_sync(5)); print("Starts immediately!")
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