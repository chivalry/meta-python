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

[Next: Virtual Environments][1]

[1]: ch_05_virtenv.md 'Chapter 5: Virtual Environments'
