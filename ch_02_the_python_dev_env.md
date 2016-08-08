The Python Development Environment
==================================

Before we can create anything with Python we need to make sure the Python interpreter is available to us. Linux users either already have Python installed or know what to do with their distribution's packaging system. Windows users will find much more [competent instructions][1] than I can provide.

Mac users, on the other hand, are in a somewhat strange situation. Apple's macOS *is* Unix, and so Apple has included Python (and Git, which we'll cover later) with their operating system for quite some time, but it's an older version, specifically, 2.7.

While there are a few procedures for installing Python 3.5, I recommend [Homebrew][2], an open source package management system for macOS. You only need two commands in the Terminal to install first Homebrew and then Python 3.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
```

Periodically, you'll want to run `brew update` and `brew upgrade python3`. Homebrew is a great system for Unixy software that Apple either neglected to include or included earlier versions as well as software libraries that might be useful. If you're unfamiliar with it, I highly suggest that you look into it beyond its utility for Python. A good place to start is [Bruno Skvorc's][3] [article][4].

[Next: Text Editing][5]

[1]: http://www.diveintopython3.net/installing-python.html#windows 'Installing Python on Windows'
[2]: http://brew.sh/ 'Homebrew'
[3]: http://tutsplus.com/authors/bruno-skvorc 'Bruno Skvorc'
[4]: http://computers.tutsplus.com/tutorials/homebrew-demystified-os-xs-ultimate-package-manager--mac-44884 'Homebrew Demystified'
[5]: ch_03_text_editing.md 'Chapter 3: Text Editing'
