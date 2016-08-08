Introduction
============

Over the last few months I've been delving deeper into Python. Generally I have trouble learning a language or technology unless I have a specific and real goal in mind while learning it. Then I had a client who needed a fairly simply text file transformation utility, and it seemed a good opportunity to learn Python. I was familiar enough with the basic syntax that writing the utility didn't require *too* much research, and I was able to use some of Python's powerful features to finish the utility in only about 50 lines of code and a few hours of work.

Having enjoyed my experience with Python, I decided to go a bit deeper and scratch an itch of my own with the language. I'm a big comic book fan, have been for forty-plus years. The most popular format for digital comic books is the [Comic Book Archive](https://en.wikipedia.org/wiki/Comic_book_archive) format, which is really just an archive file (zip, rar, tar, etc.) with a specific extension (cbz, cbr, cbt, etc.). My itch is that I wanted a utility that will make it easy for me to create and manipulate these files.

My plan was to create a library first, move from there to a command line utility and finally a GUI app, each a separate project, the latter two making use of the first. I haven't gotten there yet, although I'm still working on the project. But as I began writing code, I began to come across many Python concepts that, well, they sort of aren't Python. But that's not right. Some of the concepts *are* Python (modules and packages). Some of the concepts are Python but not Python syntax (testing, for example). Some of them aren't Python, so much as additions to Python, aimed not at enhancing the language, like Python's standard library, but at assisting the developer (virtual environments, setuptools).

The trouble, for me at least, was that all of these concepts were very intertwined, and I found it difficult to wrap my head around one part because of my ignorance of another part. I found myself wishing for a tutorial that would take me from knowing Python syntax and having written a few useful tools with the language to having made my planned comic book tool available to others in a way that made it easy for them to use.

Uh-oh. That sounds like a new itch.

This is me scratching that new itch. This is going to be the book/tutorial that I wish already existed. With that in mind, as I write this introduction, I don't know most of the topics I plan to have this book cover. I'm quite familiar with the first few sections, mostly because they are language-independent. But the further down you get in the outline/table of contents, the less I know. So this will be, at least as I get to those later sections, part tutorial and part journal.

With that in mind, the goal of this book is that by the time you finish reading it (and by the time I finish writing it), you and I will both be able to write a Python package for distribution that others can use with the existing Python community infrastructure.

Assumptions
-----------

As mentioned above, this is the book I wish I had right now. Therefore, my assumption is that you are, to a large extent, me at the start of this endeavor. Specifically:

- You've been programming for some time, either professionally or as a hobby.
- You aren't completely new to Python. You've studied the syntax and have written at least a few utilities using the language.
- You're using Python 3.5.1 (the current version as I begin this) or higher. I came to Python long after 3 was released, and have little interest in dealing with cross-version compatibility.
- You're comfortable with your operating systems' command line interface.
- You're smart. I expect much of this will be my outlining the reasons a particular tool or process is a good idea and advising you to take advantage of it, with perhaps a link or Terminal listing to move you in the right direction. But if I say something like, "Create a new account on GitHub," you don't need step-by-step instructions here.

One more assumption that may be true about you but not me. I've been using Macs for nearly 30 years, but Python is also available for Linux and Windows. I'm writing this from a Mac-user's perspective (it's *my* itch, after all). So, my further assumption is, if you're not a Mac user, you're smart enough to translate any Mac-specific statements to what works on your platform.

Structure
---------

I can imagine at least three ways to cover this material.

One could cover all of the Python syntax stuff first, including modules, packages, etc. This could be followed by Python non-syntax material, such as `unittest` and `setuptools`.The last portion would cover non-Python material, such as using git and GitHub and text editing. This isn't using that order. I think there are plenty of resources that allow anyone to follow this type of order by simply covering each topic individually.

Another order of teaching might be something I've seen a few times. "Here's a Python project folder structure and here's why it's the way it is." I've found these useful, but they already exist, and I don't think we need another one.

Instead, I'll be going in the order which one would likely use to build an actual project. First thing a developer would probably do after having an idea would be to create a git repository, and once that's done, create a virtual environment, and then open a text editor, so those are the first three items I'll cover. Through each section, however, I'll try to concentrate first on what problem is being solved and how each tool or procedure solves that problem.

This isn't perfect, because each developer would have a different order of priority. Heck, I've already broken this (as you'll soon see) by having an initial simple file before I create the repository or create the virtual environment. But the overall goal will be to cover material in the order one would come across it in an actual project.

`if not Assumptions:`
---------------------

I think that if you've read this far, most of the above assumptions are true, but if you don't already know Python, I can recommend a few resources that I found helpful:

- [Dive Into Python 3](http://www.diveintopython3.net/): Good place to learn the syntax a a bit of meta Python
- [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/): More meta Python, and a primary resource for this project
- [#python](https://www.python.org/community/irc/) at [freenode.net](http://freenode.net/): Very helpful and very smart Python people hang out here to assist you.
- [Stackoverflow](http://stackoverflow.com/): Probably the very best forum for asking programming questions.

Acknowledgements
----------------

- The helpful participants of #python on freenode.net, especially:
    - RoadrunnerWMC
    - malinoff

A Simple Project
================

For this to be a tutorial, we're going to need an actual project with actual code that actually does something.  I've seen other tutorials of this sort work with `ModuleA` and `MyClass` with `a_function`, which is fine, but I find such names to be difficult to follow.

So, after thinking for a bit about it, I decided to come up with as simple a project as I could that actually did something, perhaps even something useful, which is `polygons.py` (with thanks to [wikiHow](http://www.wikihow.com/Find-the-Area-of-Regular-Polygons) for the math behind the algorithm), the listing of which is found below.

```python
import math

class RegularPolygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    @property
    def perimeter(self):
        return self.sides * self.length

    @property
    def apothem(self):
        tan = math.tan(math.pi / self.sides)
        return self.length / (2 * tan)

    @property
    def area(self):
        return (self.apothem * self.perimeter) / 2

class Square(RegularPolygon):
    def __init__(self, length):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length ** 2

hexagon = RegularPolygon(6, 10)
print('hexagon: ' + str(hexagon.area))

square = Square(10)
print('square: ' + str(square.area))
```

Yes, it's fairly trivial, but we have something that at least looks like a real project, and it's something we can test, which will be useful later. The idea will be similar to what I was planning with the comic book archive library/command line tool/GUI app. We have some code here that performs a needed result, in this case, calculating the area of a regular polygon. We'll first translate that into a library that anyone else could use on PyPI. Then we'll create a command line tool and a GUI app, both of which will use that library.

The Python Development Environment
==================================

Mac-specific content coming now. Apple's macOS is Unix, so it includes Python by default. Unfortunately, Apple doesn't include the latest version, not by a long shot. As you probably know, Python currently has two, what shall we call them, tracks. Python 2 and Python 3. The latest version of macOS, 10.11 El Capitan, ships with Python 2.7 while the latest version is 3.5.2.

The easiest procedure for getting Python 3.5.2 is to use Homebrew, a package management system for macOS. You only need to enter two commands into the Terminal to accomplish this.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
```

Periodically, you'll want to run `brew update` and `brew upgrade python3`. Homebrew is a great system for Unixy software that Apple either neglected to include or included earlier versions as well as software libraries that might be useful. If you're unfamiliar with it, I highly suggest that you look into it beyond its utility for Python.

- Python 3
- Git
- pip

Git(Hub)
========

Many years ago our programming forefathers discovered that keeping track of revisions to a programming project was useful. It allowed multiple developers to work on a project simultaneously with less risk of conflicts, but more importantly, provided a central repository of the entire project's history, with the side-effect that any previous state of the project could be returned to if necessary.

This backup facility of version control allows for experimentation. Go ahead and try that risk development path. If it doesn't work out, just return to a known good state and start from there again. It's this safety net of source control that convinced me to begin using it. Originally I used Subversion and even ran my own Subversion server, but these days source control has evolved, and the modern source control options include primarily Git, Mercurial, and Bazaar.

Among those three, Git almost certainly has the most users, and this might be due to the popularity of GitHub, a free hosting service for Git repositories (although it does support other version control systems). In addition to the advantages provided by Git itself, GitHub also offers offsite backups of your projects, and is completely free for open source projects, which, given your plan to publish to PyPI, probably includes your project.

But perhaps the primary reason to use GitHub for your project is, that's where other programmers are going to look for it. It seems circular, but the biggest reason to store your open source project on GitHub is because open source developers store their projects on GitHub. Just like my teen kids are almost required to have Facebook accounts, programmers need to have a GitHub account.

In fact, having a GitHub account is so much of a given for programmers, I'm tempted to assume that this section is unnecessary, but, just in case, if you don't have a GitHub account, go create one. If you don't have the `git` command line tool on your system (which, I think, applies only to Windows users), go install it.

GUI Access
----------

While Git itself is a command line program, there are plenty of GUI apps available, some, such as Tower, commercial, many others free and open source, such as GitUp and GitHub's own SourceTree. I've currently settled on GitUp which provides a nice compromise between a GUI view of the repository's history and diffs for each commit while also allowing me to keep my fingers on the keyboard the entire time.

Keeping Up to Date
------------------

Like Python, Apple includes Git with macOS, but, like Python, it's an older version, in this case, 2.6.4 whereas Git is up to 2.7.4. Homebrew is again the solution.

```bash
$ brew install git
```

Virtual Environments
====================

- What do virtual environments solve?
- Which virtual environment?
- Setup instructions

Editing
=======

- You already use a text editor, right?
- I use Vim
- Vim and Python
- Other options

Modules
=======

- We already have a module
- Making module explicit

Packages
========

- Package, package or package?
- The simplest package
- More useful package

Testing
=======

Unit
----

- pytest
- What to test

Coverage
--------

- Include this?

Documentation
=============

- __doc__
- Generated documentation

Distribution
============

License
-------

- MIT

Readme
------

Version
-------

Makefile
--------

What does this solve?

Requirements
------------

setuptools
----------

PyPI
----

Command Line Tool
=================

GUI App
=======
