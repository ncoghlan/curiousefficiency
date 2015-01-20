.. title: DTCA Public Consultation - Brisbane
.. slug: dtca-public-consultation
.. date: 2015-01-20 12:41:51 UTC
.. tags: python,tech,politics
.. link: 
.. description: 
.. type: text

Over the weekend, Asher Wolf
[alerted me](https://twitter.com/Asher_Wolf/status/555909774596784129) (and
many others in the open source and cryptographic communities) to the
Australian Defence Trade Controls Act 2012, and the current public
consultation taking place around a bill proposing amendments to that act.

Being heavily involved in improving the security of open source
infrastructure like the [Python Package Index](https://pypi.python.org/)
and the
[Python 2 reference interpreter](https://www.python.org/dev/peps/pep-0466/),
working at a multinational open source vendor, and having an extensive
background in working under the constraints of the US International Traffic
in Arms regulations, Asher's concern caught my attention, since bad
legislation in this area can have significant chilling effects on legitimate
research and development activities.

As a result, I've escalated this legislation for review by the legal teams
at various open source companies and organisations, with a view to making
formal submissions to the
[public consultation process](http://www.defence.gov.au/deco/Consultation.asp)
that is open until January 30th (ready for bills to be submitted for
consideration to federal parliament on February 23rd).

However, I was also able to attend the first public consultation session
held at the University of Queensland on January 19, so these are my
impressions based primarily on that sessions and my own experiences dealing
with ITAR. I'm not a lawyer and I haven't actually *read* the legislation,
so I'm not going to pick up on any drafting errors, but I can at least speak
to the intent of the folks involved in moving this process forward.

What *not* to worry about
=========================

To folks encountering this kind of legislation for the first time, the
sheer scope of the
[Defence and Strategic Goods List](http://www.defence.gov.au/deco/DSGL.asp)
can seem absolutely terrifying. This was very clear to me from some of the
questions various academics in the room were asking.

On this particular point, I can only say: *"Don't panic"*. This isn't a
unique-to-Australia list, it's backed by a treaty called the
[Wassenaar Arrangement](http://www.wassenaar.org/) - the DSGL represents
part of the implementation of that arrangement into Australian law.

When the laws implementing that arrangement are well drafted, everyone outside
the military industrial complex (and certain easily weaponised areas of
scientific research) can pretty much ignore them, while everyone
inside the military industrial complex (and the affected areas of research)
pays very close attention to them because we like not being in jail (and
because gunrunning is bad, and bioterrorism is worse, mmm'kay?).

A heavily regulated military supply chain is already scary enough, we *really*
don't want to see the likely consequences of an unregulated one. (And if
you're tempted to make a snarky comment about the latter already being the
case, no, it really isn't. While folks can sometimes use overclassification
to avoid regulations they're supposed to be following, that still introduces
significant friction and inefficiencies into whatever they're doing. It's not
as good as people actually respecting the laws of the countries they're
supposedly defending, including genuinely meeting the requirement for
civilian authority over the military, but it's still a hell of a lot better
than nothing).

Getting back on topic, the US ITAR and crypto export control laws are
currently considered the most strict implementation of the Wassenaar
Arrangement amongst the participating nations (going beyond the requirements
of the treaty in several areas), so if you see plenty of US nationals
participating in an activity without being fined and going to jail, you can
be fairly confident that it isn't actually a controlled activity under the
DSGL (or, even if it is, permits for that specific activity will be fairly
easy to get, and the most likely consequence of not realising you need a
permit for something you're doing will be someone from your government
getting in touch to point out that you should apply for one).

There are certainly some very questionable aspects of this list (with the
perennial "favourite" being the fact the Wassenaar Arrangement does, in fact,
attempt to regulate the global trade in mathematics, which is just as stupid
and problematic as it sounds), but it's a known quantity, and one we're pretty
sure we can continue to live with (at least for the time being).

What to worry about
===================

The real problem here is that the regulations included in the 2012 Act are
*not* well drafted, and the legislated 2 year transition period from May 2013
through to May 2015 prior to the enforcement provisions kicking in is about
to run out.

The biggest problem with the 2012 act is that in trying to keep things simple
(essentially, "if its on the DSGL, you need a permit"), it ended up becoming
extraordinarily draconian, requiring a permit for things that don't require
an export license even under ITAR.

For the general public, the most significant shift in the 2015 amendment bill
is the fact that several cases around open publication of information related
to dual-use technologies shift to being allowed by default, and only in
exceptional cases would a permit be required (and in those cases, the onus
would be on the government to inform the covered individuals of that
requirement).

The amendments also include a variety of additional exemptions for little
things like making it legal for Australian's own police and security agencies
to collaborate with their international counterparts. (Snarky comment
opportunity #2: in certain areas, making such collaboration illegal seems
like a potentially attractive idea...)

That 2 year pilot was included in the original legislation as a safety
mechanism, the feedback from the associated steering group has been
extensive, and if things had gone according to plan, the relevant amendments
to the bill would have been passed last year in the spring sitting of federal
parliament, leaving DECO with at least 6 months to educate affected
organisations and individuals, and start issuing the now necessary permits
before the enforcement provisions became active in May. Unfortunately, we
currently have a federal government that views pushing a particular
ideological agenda as being more important than *actually doing their job*,
so we're now faced with the prospect of regulations that industry doesn't
want, academia doesn't want, the Australian public service don't want, and
the Australian military don't want, coming into effect anyway.

Isn't politics fun?

What DECO are (trying) to do about it
=====================================

The group tasked with untangling this particular legislative Charlie Foxtrot
is the Australian Defence Export Control Office (DECO). Their proposal for
addressing the situation hinges on two bills that they plan to put before
the next sitting of federal parliament:

* an amendment bill for the Act itself, which fixes it to be a conventional
  implementation of the Wassenaar Arrangement, in line with existing
  implementations in other Wassenaar nations (why we didn't just do that in
  the first place is beyond me, but at least DECO are trying to fix the
  mistake now)
* a second bill to delay the enactment of the enforcement provisions for
  a further six months to provide sufficient time for DECO to properly
  educate affected parties and start issuing permits

As far as I am aware, the second bill is needed primarily due to the
consideration of the first bill slipping by six months, since we're now
looking at the prospect of only having 4 weeks for DECO to start issuing
permits before the enforcement provisions come into effect. *Nobody* involved
thinks that's a good idea.

If both of those bills pass promptly, then the only cause for concern is
whether or not there are any remaining devils in the details of the
legislation itself. Member of the general public aren't going to be able to
pick those up - despite the surface similarities, legalese isn't English, and
reading it without interpreting it in the context of relevant case law can be
a good way to get yourself into trouble. Summary translations from legalese
to English by a competent lawyer are a much safer bet, although still not
perfect. (For the programmers reading this: I personally find it useful
to think of legalese as source code that runs on the language interpreter of
a given nation's legal system, while the English translations are the code
comments and documentation that anyone should be able to read if they
understand the general concepts involved).

If at least the second bill passes, then we have another 6 months to work on
a better resolution to the problem.

If *neither* bill passes, then DECO end up in a bad situation where they'll
be required by law to implement and enforce regulations that they're
convinced are a bad idea. They actually have everything in place to do that
if they have to, but they don't want this outcome, and neither does anyone
else.


What industry and academia can do about it
==========================================

While it's very short notice, the main thing industry and academia can do
is to file formal submissions with DECO as described in their overview of
the [public consultation process](http://www.defence.gov.au/deco/Consultation.asp).

There are three main things to be addressed on that front:

* ensuring federal parliament are aware of the importance of amending the
  Defence Trade Controls Act 2012 to eliminate the more draconian provisions
* ensuring federal parliament are aware of the infeasibility of putting this
  into effect on the original timeline and the need for a significant delay
  in the introduction of the enforcement provisions
* ensuring DECO are alerted to any remaining areas of concern in the
  specific drafting of the amended legislation (although I'd advise skipping
  this one if you're not a lawyer yourself - it's the functional equivalent
  of a lawyer with no training as a programmer proposing patches to the Linux
  kernel)

We were apparently asleep at the wheel when DTCA went through in 2012, so
we owe a *lot* of thanks to whoever it was that advocated for and achieved
the inclusion of the two year transition and consultation period in the
original bill. Now we need to help ensure that our currently somewhat
dysfunctional federal parliament doesn't keep us from receiving the benefit
of that foresight.


What's definitely not going to happen
=====================================

This consultation process is *not* the place to rail against the details of
the Wassenaar Arrangement or Australia's participation in it. You won't
achieve anything except to waste the time of folks that currently have a
really serious problem to fix, and a very limited window in which to fix it.

Yes, Wassenaar has some serious problems, especially around its handling
of cryptography and cryptographic research, but we have a fairly settled
approach to handling that at this point in history. The critical concern in
this current case is to help DECO ensure that the associated Australian
regulations can be readily handled through the mechanisms that have already
been put in place to handle existing Wassenaar enforcement regimes in other
countries. With the way the 2012 Act was drafted, that's almost certainly
currently not the case, but the proposed 2015 amendments *should* fix it
(assuming the amendments actually have the effects that DECO has indicated
they're intended to).
