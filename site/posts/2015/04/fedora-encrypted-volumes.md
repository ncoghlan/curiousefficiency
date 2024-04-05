.. title: Accessing TrueCrypt Encrypted Files on Fedora 22
.. slug: fedora-encrypted-volumes
.. date: 2015-04-25 22:24:15 UTC
.. tags: fedora
.. category:
.. link: 
.. description: 
.. type: text

I recently got a new ultrabook (a HP Spectre 360), which means I finally have enough space to transfer my music files from the external drive where they've been stored for the past few years back to the laptop (there really wasn't enough space for them on my previous laptop, a first generation ASUS Zenbook, but even with the Windows partition still around, the extra storage space on the new device leaves plenty of room for my music collection).

Just one small problem: the bulk of the storage on that drive was in a TrueCrypt encrypted file, and the Dolphin file browser in KDE doesn't support mounting those as volumes through the GUI (at least, it doesn't as far as I could see).

So, off to the command line we go. While TrueCrypt itself isn't readily available for Fedora due to problems with its licensing terms, the standard `cryptsetup` utility supports accessing existing TrueCrypt volumes, and the `tcplay` package also supports creation of new volumes.

In my case, I just wanted to read the music files, so it turns out that `cryptsetup` was all I needed, but I didn't figure that out until after I'd already installed `tcplay` as well.

For both `cryptsetup` and `tcplay`, one of the things you need to set up in order to access a TrueCrypt encrypted *file* (as opposed to a fully encrypted volume) is a loopback device - these let you map a filesystem block device back to a file living on another filesystem. The examples in the `tcplay` manual page (`man tcplay`) indicated the command I needed to set that up was `losetup`.

However, the `losetup` instructions gave me trouble, as they appeared to be telling me I didn't have any loopback devices:

    [ncoghlan@thechalk ~]$ losetup -f <path to encrypted file>
    losetup: cannot find an unused loop device: No such file or directory

Searching on Google for "fedora create a loop device" brought me to [this Unix & Linux Stack Exchange question](https://unix.stackexchange.com/questions/98742/how-to-add-more-dev-loop-devices-on-fedora-19) as the first result, but the answer there struck me as being far too low level to be reasonable as a prerequisite for accessing encrypted files as volumes.

So I scanned further down through the list of search results, with [this Fedora bug report](https://bugzilla.redhat.com/show_bug.cgi?id=1019440) about difficulty accessing TrueCrypt volumes catching my eye. As with the Stack Overflow answer, most of the comments there seemed to be about reverting the effect of [a change to Fedora's default behaviour](https://bugzilla.redhat.com/show_bug.cgi?id=896160) a change which meant that Fedora no longer came with any loop devices preconfigured.

However, looking more closely at Kay's original request to trim back the list of default devices revealed an interesting statement: "Loop devices can and should be created on-demand, and only when needed, losetup has been updated since Fedora 17 to do that just fine."

That didn't match my own experience with the `losetup` command, so I wondered what might be going on to explain the discrepancy, which is when it occurred to me that running `losetup` with root access might solve the problem. Generally speaking, ordinary users aren't going to have the permissions needed to create new devices, and I'd been running the `losetup` command using my normal user permissions rather than running it as `root`. That was a fairly straightforward theory to test, and sure enough, that worked:

    [ncoghlan@thechalk ~]$ sudo losetup -f <path to encrypted file>
    /dev/loop0

Armed with my new loop device, I was then able to open the TrueCrypt encrypted file on the external GoFlex drive as a decrypted volume:

    [ncoghlan@thechalk ~]$ sudo cryptsetup open --type tcrypt /dev/loop0 flexdecrypted

Actually supplying the password to decrypt the volume wasn't a problem, as I use a password manager to limit the number of passwords I need to actually *remember*, while still being able to use strong passwords for different services and devices.

However, even with my music files in the process of copying over to my laptop, this all still seemed a bit cryptic to me, even for the Linux command line. It would have saved me a lot of time if I'd been nudged in the direction of "sudo losetup -f" much sooner, rather than having to decide to ignore some bad advice I found on the internet and instead figure out a better answer by way of the Fedora issue tracker.

So I took four additional steps:

* First, I filed [a new issue](https://bugzilla.redhat.com/show_bug.cgi?id=1215370) against `losetup`, suggesting that it nudge the user in the direction of running it with root privileges if they first run it as a normal user and don't find any devices
* Secondly, I followed up on the previous issue I had found in order to [explain my findings](https://bugzilla.redhat.com/show_bug.cgi?id=1019440#c22)
* Thirdly, I added a [new answer](https://unix.stackexchange.com/a/198637/61794) to the Stack Exchange question I had found, suggesting the use of the higher level `losetup` command over the lower level `mknod` command
* Finally, I wrote this post recounting the tale of figuring this out from a combination of local system manual pages and online searches

Adding a right-click option to Dolphin to be able to automatically mount TrueCrypt encrypted files as volumes and open them would be an even nicer solution, but also a whole lot more work. The only actual *change* suggested in my above set of additional steps is tweaking a particular error message in one particular situation, which should be far more attainable than a new Dolphin feature or addon.