Introduction
============

Over the last few months I've been delving deeper into Python. Generally I have trouble learning a language or technology unless I have a specific and real goal in mind while learning it. Then I had a client who needed a fairly simply text file transformation utility, and it seemed a good opportunity to learn Python. I was familiar enough with the basic syntax that writing the utility didn't require *too* much research, and I was able to use some of Python's powerful features to finish the utility in only about 50 lines of code and a few hours of work.

Having enjoyed my experience with Python, I decided to go a bit deeper and scratch an itch of my own with the language. I'm a big comic book fan, have been for forty-plus years. The most popular format for digital comic books is the [Comic Book Archive][1] format, which is really just an archive file (zip, rar, tar, etc.) with a specific extension (cbz, cbr, cbt, etc.). My itch is that I wanted a utility that will make it easy for me to create and manipulate these files.

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

- [Dive Into Python 3][2]: Good place to learn the syntax and a bit of meta Python
- [The Hitchhiker's Guide to Python][3]: More meta Python, and a primary resource for this project
- [#python][4] at [freenode.net][5]: Very helpful and very smart Python people hang out here to assist you.
- [Stackoverflow][6]: Probably the very best forum for asking programming questions.

Acknowledgements
----------------

- The helpful participants of #python on freenode.net, especially:
    - RoadrunnerWMC
    - malinoff

[Next: A Simple Project][7]

[1]: https://en.wikipedia.org/wiki/Comic_book_archive 'Comic Book Archive at Wikipedia'
[2]: http://www.diveintopython3.net/ 'Dive Into Python 3'
[3]: http://docs.python-guide.org/en/latest/ "The Hitchhiker's Guide to Python"
[4]: https://www.python.org/community/irc/ "Python's IRC Community"
[5]: http://freenode.net/ 'freenode.net'
[6]: http://stackoverflow.com/ 'Stackoverflow'
[7]: ch_01_a_simple_project.md 'Chapter 2: A Simple Project'
