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



[Next: Text Editing][5]

[1]: http://www.diveintopython3.net/installing-python.html#windows 'Installing Python on Windows'
[2]: http://brew.sh/ 'Homebrew'
[3]: http://tutsplus.com/authors/bruno-skvorc 'Bruno Skvorc'
[4]: http://computers.tutsplus.com/tutorials/homebrew-demystified-os-xs-ultimate-package-manager--mac-44884 'Homebrew Demystified'
[5]: ch_03_text_editing.md 'Chapter 3: Text Editing'
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
