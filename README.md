Introduction
============

Over the last few months I've been delving deeper into Python. Generally I have trouble learning a language or technology unless I have a specific and real goal in mind while learning it. Recently I had a client who needed a fairly simply text file transformation utility, and it seemed a good opportunity to learn Python. I was familiar enough with the basic syntax that writing the utility didn't require *too* much research, and I was able to use some of Python's powerful features to finish the utility in only about 50 lines of code and a few hours of work.

Having enjoyed my experience with Python, I decided to go a bit deeper and scratch an itch of my own with the language. I'm a big comic book fan, have been for forty-plus years. The most popular format for digital comic books is the Comic Book Archive format, which is really just an archive file (zip, rar, tar, etc.) with a specific extension (cbz, cbr, cbt, etc.). My itch is that I want a utility that will make it easy for me to create and manipulate these files.

My plan was to create a library first, move from there to a command line utility and finally a GUI app, each a separate project, the latter two making use of the first. I haven't gotten there yet, although I'm still working on the project. But as I began writing code, I began to come across many Python concepts that, well, they sort of aren't Python. But that's not right. Some of the concepts *are* Python (modules and packages). Some of the concepts are Python but not Python syntax (testing, for example). Some of them aren't Python, so much as additions to Python, aimed not at enhancing the language, like Python's standard library, but at assisting the developer (virtual environments, setuptools).

The trouble, for me at least, was that all of these concepts were very intertwined, and I found it difficult to wrap my head around one part because of my ignorance of another part. I found myself wishing for a tutorial that would take me from knowing Python syntax and having written a few useful tools with the language to having made my planned comic book tool available to others in a way that made it easy for them to use.

Uh-oh. That sounds like a new itch.

This is me scratching that new itch. This is going to be the book/tutorial that I wish already existed. With that in mind, as I write this introduction, I don't know most of the topic I plan to have this book cover. I'm quite familiar with the first few sections, mostly because they are language-independent. But the further down you get in the outline/table of contents, the less I know. So this will be, at least as I get to those later sections, part tutorial and part journal.

With that in mind, the goal of this book is that by the time you finish reading it (and by the time I finish writing it), you and I will both be able to write a python package for distribution that others can use with the existing Python community infrastructure.

Assumptions
-----------

As mentioned above, this is the book I wish I had right now. Therefore, my assumption is that you are, to a large extent, me at the start of this endeavor. Specifically:

- You've been programming for some time, either professionally or as a hobby.
- You aren't completely new to Python. You've studied the syntax and have written at least a few utilities using the language.
- You're comfortable with your operating systems' command line interface.

One more assumption that may be true about you but not me. I've been using Macs for nearly 30 years, but Python is also available for Linux and Windows. I'm writing this from a Mac-user's perspective (it's *my* itch, after all). So, my further assumption is, if you're not a Mac user, you're smart enough to translate any Mac-specific statements to what works on your platform.

Git(Hub)
========

Editing
=======

Virtual Environments
====================

Modules
=======

Packages
========

Documentation
=============

Testing
=======

Unit
----

Coverage
--------

Distribution
============

License
-------

Readme
------

Version
-------

Makefile
--------

Requirements
------------

setuptools
----------

PyPI
----
