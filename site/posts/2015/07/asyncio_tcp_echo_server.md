.. title: TCP echo client and server in Python 3.5
.. slug: asyncio-tcp-echo-server
.. date: 2015-07-11 06:31:44 UTC
.. tags: python
.. category:
.. link: 
.. description: 
.. type: text

This is a follow-on from my
[previous post](http://www.curiousefficiency.org/posts/2015/07/asyncio-background-calls.html)
on Python 3.5's new `async`/`await` syntax. Rather than the simple background
timers used in the original post, this one will look at the impact native
coroutine support has on the TCP echo client and server examples from the
[asyncio documentation](https://docs.python.org/3.4/library/asyncio-stream.html#tcp-echo-client-using-streams).

First, we'll recreate the `run_in_foreground` helper defined in the previous
post. This helper function makes it easier to work with coroutines from
otherwise synchronous code (like the interactive prompt):

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

Next we'll define the coroutine for our TCP echo server implementation,
which simply waits to receive up to 100 bytes on each new client connection,
and then sends that data back to the client:

    :::python
    async def handle_tcp_echo(reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("-> Server received %r from %r" % (message, addr))
        print("<- Server sending: %r" % message)
        writer.write(data)
        await writer.drain()
        print("-- Terminating connection on server")
        writer.close()

And then the client coroutine we'll use to send a message and wait for a
response:

    :::python
    async def tcp_echo_client(message, port, loop=None):
        reader, writer = await asyncio.open_connection('127.0.0.1', port,
                                                            loop=loop)
        print('-> Client sending: %r' % message)
        writer.write(message.encode())
        data = (await reader.read(100)).decode()
        print('<- Client received: %r' % data)
        print('-- Terminating connection on client')
        writer.close()
        return data

We then use our `run_in_foreground` helper to interact with these coroutines
from the interactive prompt. First, we start the echo server:

    :::pycon
    >>> make_server = asyncio.start_server(handle_tcp_echo, '127.0.0.1')
    >>> server = run_in_foreground(make_server)

Conveniently, since this is a coroutine running in the *current* thread, rather
than in a different thread, we can retrieve the details of the listening
socket immediately, including the automatically assigned port number:

    :::pycon
    >>> server.sockets[0]
    <socket.socket fd=6, family=AddressFamily.AF_INET, type=2049, proto=6, laddr=('127.0.0.1', 40796)>
    >>> port = server.sockets[0].getsockname()[1]

Since we haven't needed to hardcode the port number, if we want to define a
second server, we can easily do that as well:

    :::pycon
    >>> make_server2 = asyncio.start_server(handle_tcp_echo, '127.0.0.1')
    >>> server2 = run_in_foreground(make_server2)
    >>> server2.sockets[0]
    <socket.socket fd=7, family=AddressFamily.AF_INET, type=2049, proto=6, laddr=('127.0.0.1', 41200)>
    >>> port2 = server2.sockets[0].getsockname()[1]

Now, both of these servers are configured to run directly in the main thread's
event loop, so trying to talk to them using a synchronous client wouldn't work.
The client would block the main thread, and the servers wouldn't be able to
process incoming connections. That's where our asynchronous client coroutine
comes in: if we use *that* to send messages to the server, then it doesn't
block the main thread either, and both the client and server coroutines can
process incoming events of interest. That gives the following results:

    :::pycon
    >>> print(run_in_foreground(tcp_echo_client('Hello World!', port)))
    -> Client sending: 'Hello World!'
    -> Server received 'Hello World!' from ('127.0.0.1', 44386)
    <- Server sending: 'Hello World!'
    -- Terminating connection on server
    <- Client received: 'Hello World!'
    -- Terminating connection on client
    Hello World!

Note something important here: you will get *exactly* that sequence of
output messages, as this is *all* running in the interpreter's main thread, in
a deterministic order. If the servers were running in their own threads, we
wouldn't have that property (and reliably getting access to the port numbers
the server components were assigned by the underlying operating system would
also have been far more difficult).

And to demonstrate both servers are up and running:

    :::pycon
    >>> print(run_in_foreground(tcp_echo_client('Hello World!', port2)))
    -> Client sending: 'Hello World!'
    -> Server received 'Hello World!' from ('127.0.0.1', 44419)
    <- Server sending: 'Hello World!'
    -- Terminating connection on server
    <- Client received: 'Hello World!'
    -- Terminating connection on client
    Hello World!

That then raises an interesting question: how would we send messages to the
two servers in parallel, while still only using a single thread to manage the
client and server coroutines? For that, we'll need our another of our helper
functions from the previous post, `schedule_coroutine`:

    :::python
    def schedule_coroutine(target, *, loop=None):
        """Schedules target coroutine in the given event loop

        If not given, *loop* defaults to the current thread's event loop

        Returns the scheduled task.
        """
        if asyncio.iscoroutine(target):
            return asyncio.ensure_future(target, loop=loop)
        raise TypeError("target must be a coroutine, "
                        "not {!r}".format(type(target)))


**Update:** *As with the previous post, this post originally suggested a
combined "run_in_background" helper function that handled both scheduling
coroutines and calling arbitrary callables in a background thread or process.
On further reflection, I decided that was unhelpfully conflating two different
concepts, so I replaced it with separate "schedule_coroutine" and
"call_in_background" helpers*


First, we set up the two client operations we want to run in parallel:

    :::pycon
    >>> echo1 = schedule_coroutine(tcp_echo_client('Hello World!', port))
    >>> echo2 = schedule_coroutine(tcp_echo_client('Hello World!', port2))

Then we use the `asyncio.wait` function in combination with `run_in_foreground`
to run the event loop until both operations are complete:

    :::pycon
    >>> run_in_foreground(asyncio.wait([echo1, echo2]))
    -> Client sending: 'Hello World!'
    -> Client sending: 'Hello World!'
    -> Server received 'Hello World!' from ('127.0.0.1', 44461)
    <- Server sending: 'Hello World!'
    -- Terminating connection on server
    -> Server received 'Hello World!' from ('127.0.0.1', 44462)
    <- Server sending: 'Hello World!'
    -- Terminating connection on server
    <- Client received: 'Hello World!'
    -- Terminating connection on client
    <- Client received: 'Hello World!'
    -- Terminating connection on client
    ({<Task finished coro=<tcp_echo_client() done, defined at <stdin>:1> result='Hello World!'>, <Task finished coro=<tcp_echo_client() done, defined at <stdin>:1> result='Hello World!'>}, set())

And finally, we retrieve our results using the `result` method of the task
objects returned by `schedule_coroutine`:

    :::pycon
    >>> echo1.result()
    'Hello World!'
    >>> echo2.result()
    'Hello World!'

We can set up as many concurrent background tasks as we like, and then use
`asyncio.wait` as the foreground task to wait for them all to complete.

But what if we had an existing blocking client function that we wanted or
needed to use (e.g. we're using an `asyncio` server to test a synchronous
client API). To handle that case, we use our third helper function from the
previous post:

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

To explore this, we'll need a blocking client, which we can build based on
Python's existing
[socket programming HOWTO guide](https://docs.python.org/3/howto/sockets.html):

    :::python
    import socket
    def tcp_echo_client_sync(message, port):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('-> Client connecting to port: %r' % port)
        conn.connect(('127.0.0.1', port))
        print('-> Client sending: %r' % message)
        conn.send(message.encode())
        data = conn.recv(100).decode()
        print('<- Client received: %r' % data)
        print('-- Terminating connection on client')
        conn.close()
        return data

We can then use `functools.partial` in combination with `call_in_background` to
start client requests in multiple operating system level threads:

    :::pycon
    >>> query_server = partial(tcp_echo_client_sync, "Hello World!", port)
    >>> query_server2 = partial(tcp_echo_client_sync, "Hello World!", port2)
    >>> bg_call = call_in_background(query_server)
    -> Client connecting to port: 35876
    -> Client sending: 'Hello World!'
    >>> bg_call2 = call_in_background(query_server2)
    -> Client connecting to port: 41672
    -> Client sending: 'Hello World!'

Here we see that, unlike our coroutine clients, the synchronous clients have
started running immediately in a separate thread. However, because the event
loop isn't currently running in the main thread, they've blocked waiting for
a response from the TCP echo servers. As with the coroutine clients, we
address that by running the event loop in the main thread until our clients
have both received responses:

    :::pycon
    >>> run_in_foreground(asyncio.wait([bg_call, bg_call2]))
    -> Server received 'Hello World!' from ('127.0.0.1', 52585)
    <- Server sending: 'Hello World!'
    -- Terminating connection on server
    -> Server received 'Hello World!' from ('127.0.0.1', 34399)
    <- Server sending: 'Hello World!'
    <- Client received: 'Hello World!'
    -- Terminating connection on server
    -- Terminating connection on client
    <- Client received: 'Hello World!'
    -- Terminating connection on client
    ({<Future finished result='Hello World!'>, <Future finished result='Hello World!'>}, set())
    >>> bg_call.result()
    'Hello World!'
    >>> bg_call2.result()
    'Hello World!'
