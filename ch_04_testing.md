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

[Next: Documentation][1]

[1]: ch_05_docs.md 'Chapter 5: Documentation'
[2]: http://doc.pytest.org/en/latest/index.html 'pytest'
[3]: http://junit.org/junit4/ 'JUnit'
[4]: https://docs.python.org/3/library/unittest.html 'unittest'

<!--
REF: https://schettino72.wordpress.com/2008/01/19/11/
REF: http://doc.pytest.org/en/latest/example/pythoncollection.html
-->
