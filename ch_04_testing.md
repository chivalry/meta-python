Testing
=======

Automated testing is an enormous topic. In this chapter we're not going to deal with it in a manner anywhere approaching exhaustive. Instead, we're going to show you how to integrate testing with your package by creating a few test suites. These tests can be used yourself and specified in your package definition so that others can easily use them as well.

We're also not going to go into details about the philosophy unit testing or test driven development. Personally, I like testing, but I remain unconvinced of the dichotomy between "unit testing," "integration testing," etc. Our only goal here will be to take some tests we want to perform on our code (which will, in fact, be unit tests) and integrate the execution of those tests into our project.

> TODO: Investigate coverage testing

Python has a long history of available testing frameworks. [`unittest`][4], a unit testing framework based on [JUnit][3] was originally an external module that programmers had to install, but it was integrated as a built-in module some time ago. However, some users consider it, perhaps due to it's Java heritage, to be rather "unpythonic," and I have to agree. It requires quite a bit of boilerplate code to get working, among other limitations, and [pytest][2] was written to overcome these shortcomings, but requires manual installation using `pip`, Python's built-in package manager (which we'll cover in more detail later).

Get back into your Terminal, `cd` into the `polygon` project folder, and make sure your virtual environment is activated.

```bash
~ $ cd polygons

polygons $ activate
(venv)
polygons $ pip install pytest
Collecting pytest
  Using cached pytest-2.9.2-py2.py3-none-any.whl
Collecting py>=1.4.29 (from pytest)
  Using cached py-1.4.31-py2.py3-none-any.whl
Installing collected packages: py, pytest
Successfully installed py-1.4.31 pytest-2.9.2
(venv)
polygons $ pip freeze
py==1.4.31
pytest==2.9.2
(venv)
polygons $ py.test
=============================== test session starts =================================
platform darwin -- Python 3.5.2, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /Users/chuck/polygons, inifile: 
collected 0 items 

============================ no tests ran in 0.46 seconds ============================
(venv)
polygons $
```

`pytest` requires the `py` module, and `pip` takes care of installing both for us, as demonstrated by the `pip freeze` command, which lists the modules `pip` has installed. Then, just to make sure everything's working correctly, we execute `py.test`, which searches through the current directory and subdirectories looking for tests to execute. Since we haven't written any, none were found, but we can see that `pytest` is working.

What Should We Test?
--------------------

We already know that our multi-file module works as expected, at least given the `test.py` file we wrote earlier. But it's rather fragile, especially if it's going to be published for others to use. For example, we don't yet have any parameter checking to ensure the number of angles and lengths given for a polygon match the number of sides. (We also don't check that the values of lengths and angles given produce a closed polygon, but algorithms to check such things are rather complex and beyond the scope of this book.)

We'll start out with a list of things that should be true of our polygons, regular polygons, etc.

- `Polygon` should raise an error if:
    - `sides` is not an `int`
    - `lengths` is not a `list`
    - `angles` is not a `list`
    - The count of `lengths` or `angles` is not equal to `sides`
    - Any value in `lengths` or `angles` is non-numeric
    - The sum of `angles` is not equal to `(sides - 2) * 180`
    - Any value in `lengths` is less than or equal to zero
    - Any value in `angles` is less than or equal to zero or greater than or equal to 180
- `RegularPolygon` should raise an error if `sides` is not an int, `length` is non-numeric or if either is less than or equal to zero, but these conditions are already covered by the `Polygon` class. Similar testing can be eliminated for `EquilateralTriangle` and `Square`.
- We should get the appropriate polygon names back based on the number of sides.
- The area of a square should always be the square of a side, even if we've initiated a `RegularPolygon` object with 4 sides instead of a `Square` object.
- The above rule holds for equilateral triangles that have been initiated as `RegularPolygon` objects as well.
- An equilateral triangle with a side length of $\sqrt[4]{3}$ should have an area of $3/4$.

More Folder Structure
---------------------

Like most things in programming, there are many ways we can structure our test suite within our folder structure. My preference is to keep all the tests in their own folder within the project folder and have a separate test file for each module file. This will give a folder structure like this:

```
polygons
    polygons
        __init__.py
        polygon
            __init__.py
            polygon.py
        regularpolygon
            __init__.py
            regularpolygon.py
            square.py
            equilateraltriangle.py
    tests
        test_polygon.py
        test_regularpolygon.py
        test_square.py
        test_equilateraltriangle.py
    README.md
    .git
    venv
```

For the time being, `test_regularpolygon.py` is going to be empty because all the tests I've thought of for `RegularPolygon` are covered by testing `Polygon`. But I'll keep the file there for no other reason than to remind myself that I haven't *forgotten* about testing `RegularPolygon`.

Making Our Package Available to Out Tests
-----------------------------------------

Before we can write and use our tests, we have a problem to solve. Our `test_*` files can't see the `polygons` multi-file module because the `tests` and `polygons` directories are at the same level. You can confirm this, if you like, by placing `import polygons` at the top of `test_polygon.py`. When you attempt to perform your tests with `py.test`, you'll receive an `ImportError` message that there is no module named `polygons`.

While there are multiple ways to solve this, such as manually or programmatically editing the `PYTHONPATH` environment variable, we're going to create a minimal `setup.py` file and use `pip` to install our multi-file package in "editable" mode. `pip` can install any package it can access, either locally or over the Internet (such as on GitHub), not just those on the PyPI. If we add a `setup.py` file to our directory structure, `polygons` becomes a package (in the distribution sense). Eventually our `setup.py` file will have many details in it, but for now, it only needs a few lines.

Using `pip` to install a package in editable mode means that the packages is available (within the virtual environment) to any Python file, just like any package installed with `pip`, but changes made to the code of your package are immediately available and don't have to be re-installed.

Create a new file, `setup.py`, in the root level of your project, and give it the following content:

```python
from setuptools import setup

setup(
    name='polygons',
    packages=find_packages()
)
```

`setuptools` is a built-in Python module that's integral to dealing with Python packages. We'll become more familiar with it in a future chapter. For now, get into the Terminal and enter the following command while in your project directory:

```bash
pip install --editable . # "pip install -e ." works as well
```

Here we're using `.` to indicate the current directory, which is a project directory, so the above line has the effect of installing our `polygons` package in our virtual environment. If you added `import polygons` to `test_polygon.py`, you can now run `py.test` again without getting the `ImportError`. Now that we have this working, feel free to delete the `tests.py` file.

You'll notice that running the command gave us a new folder, `polygons.egg-info`, which is one of the formats available for Python eggs. Python eggs, in turn, are distributed Python packages. For eggs that you install from PyPI, the format would probably be a zip file with a `.egg` extension, but in this case, the editable option of `pip install` created a folder with information about our local package. Feel free to take a look inside the files within `polygons.egg-info`. Just don't make any changes.

On last point before we move forward. Although `pip` can uninstall most packages, editable packages are the exception. If you want to remove the editable install, you'll need to perform two actions:

- Delete the `polygons.egg-info` directory.
- Remove the path to your project directory from the file found at `venv/lib/python3.5/site-packages/easy-install.pth`.

[Next: Documentation][1]

[1]: ch_05_docs.md 'Chapter 5: Documentation'
[2]: http://doc.pytest.org/en/latest/index.html 'pytest'
[3]: http://junit.org/junit4/ 'JUnit'
[4]: https://docs.python.org/3/library/unittest.html 'unittest'

<!--
REF: https://schettino72.wordpress.com/2008/01/19/11/
REF: http://doc.pytest.org/en/latest/example/pythoncollection.html
REF: https://packaging.python.org/distributing/
REF: https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode
REF: http://www.siafoo.net/article/77#install-vs-develop
REF: https://wiki.python.org/moin/PythonPackagingTerminology
-->
