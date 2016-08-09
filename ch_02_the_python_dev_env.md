The Python Development Environment
==================================

Install Python 3
----------------

Before we can create anything with Python we need to make sure the Python interpreter is available to us. Linux users either already have Python installed or know what to do with their distribution's packaging system. Windows users will find much more [competent instructions][1] than I can provide.

Mac users, on the other hand, are in a somewhat strange situation. Apple's macOS *is* Unix, and so Apple has included Python (and Git, which we'll cover later) with their operating system for quite some time, but it's an older version, specifically, 2.7.

While there are a few procedures for installing Python 3.5, I recommend [Homebrew][2], an open source package management system for macOS. You only need two commands in the Terminal to install first Homebrew and then Python 3.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
```

Periodically, you'll want to run `brew update` and `brew upgrade python3`. Homebrew is a great system for Unixy software that Apple either neglected to include or included earlier versions as well as software libraries that might be useful. If you're unfamiliar with it, I highly suggest that you look into it beyond its utility for Python. A good place to start is [Bruno Skvorc's][3] article [Homebrew Demystified][4], followed by [good advice][6] from [Shannon Appelcline][7].

Text Editing
------------

While I doubt that I need to mention this, writing Python requires a text editor and although it probably won't make a difference to the rest of this material, I use [Vim][8] for all of my text editing. If you haven't yet chosen a text editor, I can't recommend Vim enough.

- It's designed with the programmer in mind and allows you to keep you fingers on the keyboard for everything, no menus or pointer moving required.
- It's available for every platform, and regardless of whether chosen macOS, Linux or Windows, there will come a time when you need to use something else, such as when you need to SSH into a server. Vim is installed by default on macOS and Linux and can be easily added to Windows.
- It comes with built-in Python syntax detecting and highlighting.
- Anything it doesn't do it can be made to do, either with any of hundreds of [plugins][9] or by [writing your own][10].
- Regardless of the advantages of Python, it's likely that you'll spend at least some time using another language. By using a generic text editor instead of a [Python IDE][11] you won't have to switch mental states when working with text that isn't Python.

And yes, again, macOS does come with Vim installed, but it's an older version and you may want the MacVim GUI app, and, again, Homebrew comes to the rescue.

```bash
$ brew install macvim --override-system-vim
$ brew linkapps macvim
```

This will install the latest MacVim and use the version of Vim it comes with as the default when you type `vim` in the terminal. That last line will place a symlink of the Homebrew installed MacVim into `/Applications`, which, yes, should have happened automatically.

> TODO: Investigate `brew install vim --with-python3`

> TODO: Investigate http://mikegrouchy.com/blog/2012/05/compile-vim-with-python-support-on-osx-with-homebrew.html

Git(Hub)
--------

Like using a text editor, using Git and GitHub should be a given. But if you need convincing, [James Bruce][12] provides some [justification for Git][13] while [Karl Broman][14] is [more succinct and includes GitHub][15].

See if this story sounds familiar. Apple includes Git on macOS, but it's not the most recent version, and Homebrew makes it easy to bypass that limitation.

```bash
brew install git
```

Seriously, Homebrew rocks.

As far as a GUI interface into Git, I've chosen [GitUp][16]. It's got a sparse interface that I appreciate, is completely controllable from the keyboard, but doesn't require that I remember all those Git commands.

Virtual Environments
--------------------

Here we come to the first topic that I was unfamiliar with when I began this journey, which is probably why I'll go into a bit more detail now. If you're me, this is where you start actually needing assistance.

First, the problem: The Python community is quite dynamic. Python itself is actively being developed with frequent updates, and there are hundreds of available libraries, which is great, because it severely reduces the likelihood that you'll have to reinvent the wheel for some solved problem. And these libraries are frequently updated, which is also great, because they get incrementally better, faster, and more bug free.

Taking advantage of all this work that others have done, you create your Python program with Python 3.5.1 and [simplejson][17] 3.8.1. Everything is going smoothly as you build your software, but then you notice that Python 3.5.2 is out, and you want the latest and greatest Python, so you install it. And simplejson just added some features that sound interesting, so you update that too.

OK, updates are finished, back to your own work. You run your tests before you do anything new and find your tests failing. Something's broken? But you haven't changed any of your code since the last time it worked.

Yes, this is all contrived, but you get the point. Your program worked but something in one of those updates broke it. Going backwards to the versions that work with your program isn't exactly fun. Figuring out which one of them broke the software isn't fun either. And Python is supposed to be fun!

This is the problem virtual environments solve. If you're familiar with Perl, Ruby or Haskel, you might be familiar with [`local::lib`][18], [`bundler`][19], or [sandboxes][20], respectively. Virtual environments provide the same feature in Python.

The concept of virtual environments proved useful and popular enough that Python began including the [`venv`][21] module with version 3.3, so nothing need be done here given our prior installation of Python 3.5, but with an understanding of the utility and necessity of virtual environments, we can move forward.

Putting the Pieces Together
---------------------------

We've got Python 3 installed, have chosen a text editor, have Git and GitHub ready, and know what virtual environments will do for us. Time to put it all together.

1. Go onto your GitHub account and create a new repository called `polygons`. Take advantage of GitHubs's automation and let the site create a README and a `.gitignore` for you targeted at Python projects.

![Creating the GitHub repository][22]

2. Once you have your new repository, use the "Clone or Download" popup menu to copy the repository's URL.

![Get your repository's URL for cloning][23]

[Next: Modules][5]

[1]: http://www.diveintopython3.net/installing-python.html#windows 'Installing Python on Windows'
[2]: http://brew.sh/ 'Homebrew'
[3]: http://tutsplus.com/authors/bruno-skvorc 'Bruno Skvorc'
[4]: http://computers.tutsplus.com/tutorials/homebrew-demystified-os-xs-ultimate-package-manager--mac-44884 'Homebrew Demystified'
[5]: ch_03_modules.md 'Chapter 3: Text Editing'
[6]: https://www.safaribooksonline.com/blog/2014/03/18/keeping-homebrew-date/ 'Keeping Your Homebrew Up to Date'
[7]: http://www.skotos.net/about/staff/shannon_appelcline.php 'About Shannon Appelcline'
[8]: http://www.vim.org/ 'Vim'
[9]: https://github.com/chivalry/vimrc/tree/master/.vim/bundle 'My own list of installed Vim plugins'
[10]: http://stevelosh.com/blog/2011/09/writing-vim-plugins/ 'Writing Vim Plugins'
[11]: https://www.jetbrains.com/pycharm/download/ 'PyCharm IDE'
[12]: http://www.makeuseof.com/tag/author/jbruce/ 'James Bruce'
[13]: http://www.makeuseof.com/tag/git-version-control-youre-developer/ 'What Is Git & Why You Should Use Version Control If You’re a Developer'
[14]: http://kbroman.org/ 'Karl Broman'
[15]: http://kbroman.org/github_tutorial/pages/why.html 'Why git and github?'
[16]: http://gitup.co/ 'GitUp Home'
[17]: https://pypi.python.org/pypi/simplejson/3.8.1 'simplejson'
[18]: http://search.cpan.org/~haarg/local-lib-2.000019/lib/local/lib.pm 'local::lib'
[19]: http://bundler.io/ 'Bundler'
[20]: http://coldwa.st/e/blog/2013-08-20-Cabal-sandbox.html 'Cabal Sandboxes'
[21]: https://docs.python.org/3/library/venv.html 'venv'
[22]: images/ch_02_fig_01.png 'Creating the GitHub repository'
[23]: images/ch_02_fig_02.png "Get your repository's URL for cloning"
