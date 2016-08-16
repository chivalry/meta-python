Testing
=======

Automated testing is an enormous topic. In this chapter we're not going to deal with it in a manner anywhere approaching exhaustive. Instead, we're going to show you how to integrate testing with your package by creating a few test suites. These tests can be used yourself and specified in your package definition so that others can easily use them as well.

We're also not going to go into details about the philosophy unit testing or test driven development. Personally, I like testing, but I remain unconvinced of the dichotomy between "unit testing," "integration testing," etc. Our only goal here will be to take some tests we want to perform on our code (which will, in fact, be unit tests) and integrate the execution of those tests into our project.

> TODO: Investigate coverage testing

Python has a long history of available testing frameworks. [`unittest`][4], a unit testing framework based on [JUnit][3], was originally an external module that programmers had to install, but it was integrated as a built-in module some time ago. However, some users consider it, perhaps due to it's Java heritage, to be rather "unpythonic," and I have to agree. It requires quite a bit of boilerplate code to get working, among other limitations, and [pytest][2] was written to overcome these shortcomings, but requires manual installation using `pip`, Python's built-in package manager (which we'll cover in more detail later).

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

Obviously, this isn't an exhaustive list of things we should test, but it's a sufficiently large number to give us some tests to integrate that isn't trivial.

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

Editing `test_polygon.py`
-------------------------

Since we don't have any argument checking yet, we'll do a little bit of test driven development and write the tests for that first. The testing we're doing here is rather simple, so I suggest that if you're unfamiliar with pytest that you take a look at the [documentation][5] for additional information, such as how tests are discovered and how to create fixtures.

Edit `test_polygon.py` to the following.

```python
from polygons.polygon import Polygon
import pytest

def test_side_requires_int():
    with pytest.raises(ValueError):
        Polygon(3.14, [5, 5, 5], [60, 60, 60])

def test_lengths_requires_list():
    with pytest.raises(ValueError):
        Polygon(3, 5, [60, 60, 60])

def test_angles_requires_list():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], 1)

def test_length_count_requires_sides_value():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5, 5], [60, 60, 60])

def test_angles_count_requires_sides_value():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], [60, 60])

def test_lengths_must_be_numeric():
    with pytest.raises(ValueError):
        Polygon(3, ['5', 5, 5], [60, 60, 60])

def test_angles_must_be_numeric():
    with pytest.raises(ValueError):
        Polygon(3, [1, 2, 3], ['60', 60, 60])

def test_angles_must_sum_correctly():
    with pytest.raises(ValueError):
        Polygon(5, [6, 6, 6, 6, 6], [120, 120, 120, 120, 120])

def test_lengths_must_be_positive():
    with pytest.raises(ValueError):
        Polygon(3, [0, 5, 5], [60, 60, 60])

def test_angles_must_be_positive():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], [0, 60, 60])
```

If you run `py.test` now, you'll get 10 failures because we haven't written any code yet for parameter checking. Here's the updated `polygon.py` to fix all those errors.

```python
class Polygon:
    names = {
            3: 'triangle',
            4: 'quadrilateral',
            5: 'pentagon',
            6: 'hexagon',
            7: 'heptagon',
            8: 'octagon',
            9: 'nonagon',
            10: 'decagon',
    }

    def __init__(self, sides:int, lengths:list, angles:list):
        self.sides = sides
        self.lengths = lengths
        self.angles = angles
        
        self.confirm_attributes()

    @property
    def perimeter(self):
        return sum(self.lengths)

    @property
    def name(self):
        return self.names[self.sides]

    def confirm_attributes(self):
        if (not isinstance(self.sides, int)) and (not self.sides.is_integer()):
            raise ValueError('sides must be an integer')

        if type(self.lengths) is not list:
            raise ValueError('lengths must be a list')
        if len(self.lengths) != self.sides:
            raise ValueError('lengths count must equal number of sides')
        if not all(isinstance(length, (int, float)) for length in self.lengths):
            raise ValueError('lengths must be numeric')
        if not all(length > 0 for length in self.lengths):
            raise ValueError('lengths must be positive')

        if type(self.angles) is not list:
            raise ValueError('angles must be a list')
        if len(self.angles) != self.sides:
            raise ValueError('angles count must equal number of sides')
        if not all(isinstance(angle, (int, float)) for angle in self.angles):
            raise ValueError('angles must be numeric')
        if sum(self.angles) != ((self.sides - 2) * 180):
            raise ValueError('angles must sum correctly')
        if not all(angle > 0 for angle in self.angles):
            raise ValueError('angles must be positive')
```

The only tests needed for `RegularPolygon` are to make sure that it returns an exact square when the number of sides is 4, and to make sure that it uses the equilateral triangle algorithm to calculate that polygon's area. Here's the test code to place into `test_regularpolygon.py`:

```python
import math
from polygons.regularpolygon import RegularPolygon
from polygons.regularpolygon import EquilateralTriangle

def test_square_returns_squared_side_for_area():
    assert RegularPolygon(4, 5).area == 25

def test_triangle_returns_correct_area():
    poly_area = RegularPolygon(3, 5).area
    tri_area = EquilateralTriangle(5).area
    assert math.isclose(poly_area, tri_area, rel_tol=1e-10)
```

The second test above is testing that a triangle defined as a `RegularPolygon` object will have the same returned area as that returned by an identically dimensioned `EquilateralTriangle` to within 10 decimal points.

If you run `py.test` after saving the above into `test_regularpolygon.py`, the test will fail because, by default, `RegularPolygon.area` using `math.tan` to compute the area (and returns 25.000000000000004, which, while very *close* to 25, isn't 25), which is necessary for most polygons, but for a square we can just compute the square of a side.

I don't yet know the "pythonic" way to solve this, so until I find a better method, I'm editing `RegularPolygon.area` to read as follows:

```python
@property
def area(self):
    if self.sides == 4:
        return self.length ** 2
    else:
        return (self.apothem * self.perimeter) / 2
```

For `test_square.py`, we'll just make sure that a few tests ensure we're getting the right perimeter and area.

```python
from polygons.regularpolygon import Square
import math

def test_square_perimeter():
    assert Square(1).perimeter == 4
    assert Square(5).perimeter == 20
    assert Square(1.25).perimeter == 5

def test_square_area():
    assert Square(1).area == 1
    assert Square(5).area == 25
    assert math.isclose(Square(1.5).area, 2.25, rel_tol=1e-2)
```

Finally, `test_equilateraltriangle.py` needs only one test, making sure that for a equilateral triangle of length $sqrt[4]{3}$, the area is $3/4$, again using `math.isclose` to compare `float` values.

```python
import math
from polygons.regularpolygon import EquilateralTriangle

def test_equilateral_triangle_area():
    assert math.isclose(EquilateralTriangle(3 ** (1/4)).area, 3/4, rel_tol=1e-2)
```

[Next: Documentation][1]

[1]: ch_05_docs.md 'Chapter 5: Documentation'
[2]: http://doc.pytest.org/en/latest/index.html 'pytest'
[3]: http://junit.org/junit4/ 'JUnit'
[4]: https://docs.python.org/3/library/unittest.html 'unittest'
[5]: http://doc.pytest.org/en/latest/index.html 'pytest'

<!--
REF: https://schettino72.wordpress.com/2008/01/19/11/
REF: http://doc.pytest.org/en/latest/example/pythoncollection.html
REF: https://packaging.python.org/distributing/
REF: https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode
REF: http://www.siafoo.net/article/77#install-vs-develop
REF: https://wiki.python.org/moin/PythonPackagingTerminology
REF: http://pythontesting.net/framework/pytest/pytest-introduction/
-->
