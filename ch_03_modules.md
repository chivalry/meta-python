Modules (and Packages)
======================

In simplest terms, a Python module is some code that can be loaded by Python and made available to other Python code. Our `polygons.py` file is already making use of a standard module, `math`, to gain access to the `tan` and `sqrt` functions and `pi` property.

Strictly speaking, any Python file is a module. You can confirm this for yourself by opening the Python interpreter while in the `polygon` directory for the project.

```
~ $ cd polygons
polygons $ activate
(venv) 
polygons $ python
>>> import polygons
hexagon area: 259.80762113533166
hexagon name: hexagon
hexagon angles: [120.0, 120.0, 120.0, 120.0, 120.0, 120.0]
square area: 100
triangle area: 35.074028853269766
>>> quit()
(venv) 
polygons $  
```

> Note: Even if you're on macOS, your shell prompt may look a bit different from mine. I've customized by shell prompt to insert a blank line after each command as I find it easier to read. In case you're interested in how I did this, I have the following line in `~/.bash_profile`: `PS1="\n\W \$ "`. Once the virtual environment is activated, it temporarily edits the prompt to place the name of the virtual environment before the default prompt, so that while the virtual environment is active, `echo $PS1` returns `(venv) \n\w \$ `. This only happens for the current shell instance (so you won't see the different prompt if you create a new shell) and until you `deactivate` the virtual environment or close the current session.

We can see that the `import` directive loaded the code in `polygons.py` and executed it, which is why we get the report of the various polygon attributes.

Generally, when we place `print` statements in our modules like we have at the end of `polygons.py`, we don't want that code to execute when the module is imported. We could delete the code, but it's kind of nice to have the easy test of entering `python polygons.py` and getting that printout to confirm that everything is working correctly. No, it's not a full test suite, but it is a quick confirmation.

Python's way to have the best of both worlds is to check the `__name__` attribute. If we execute the module directly, `__name__` will have a value of `'__main__'`. If we import the module, `__name__` will have the name of the module. So our edit is pretty easy. We wrap those last few lines within an `if __name__ == '__main__':` block:

```python
if __name__ == '__main__':
    hexagon = RegularPolygon(6, 10)
    print('hexagon area: ' + str(hexagon.area))
    print('hexagon name: ' + hexagon.name)
    print('hexagon angles: ' + str(hexagon.angles))

    square = Square(10)
    print('square area: ' + str(square.area))

    triangle = EquilateralTriangle(9)
    print('triangle area: ' + str(triangle.area))
```

Now, if we import the module, we won't see the print statements being executed, and by printing the `__name__` attribute we can see why.

```
>>> import polygons
>>> print(polygons.__name__)
polygons
>>> 
```

The final point of all the above is, we don't have to do anything special to make our existing Python file a module. It already is. We can make it slightly better by checking for the value of the `__name__` attribute, but we can already `import` it into other Python projects and take advantage of the code we find there.

```
>>> import polygons
>>> print(polygons.RegularPolygon(5, 15).area)
387.10741513251753
>>> print(polygons.Square(12).area)
144
```

Packages (Multi-File Modules)
-----------------------------

The word "package" unfortunately has two distinct meanings in the Python community.

<dl> <dt>Package</dt>
  <dd>1. A directory of modules that also contains a `__init__.py` file</dd>
  <dd>2. A published Python library available for easy installation and use</dd> </dl>

This book deals with producing the second of those definitions while this chapter deals with creating the first. Both of these definitions are quite entrenched in the Python community, so I doubt that the problem will be resolved any time soon. [Mark Pilgrim][2] uses the term ["multi-file module"][3] when he means the first definition, but this seems awkward, although I don't have a better solution. But finding a different term for the first definition seems wise, since PyPI is short for "Python *Package* Index."

So, "a directory of modules that also contains a `__init__.py` file." Let's pretend that `polygons.py` is much larger, with more than just two simple classes. That would move us to break that file up into multiple files, perhaps one with each class.

Create a new `polygons` directory within our larger `polygons` git repository directory and create a new `__init__.py` file (the `touch` tool in the shell will do this nicely on Unix). The file only need be present for this to be a multi-file module. It doesn't have to have any contents, although we'll add some later.

```bash
(venv) 
polygons $ mkdir polygons
(venv) 
polygons $ touch polygons/__init__.py
(venv) 
polygons $
```

Now create `regularpolygon.py` in our new (not upper-level) `polygons` directory, and give it the following listing:

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

if __name__ == '__main__':
    hexagon = RegularPolygon(6, 10)
    print('hexagon: ' + str(hexagon.area))
```

Create `square.py` in the same directory with the following listing:

```python
import math

from . import regularpolygon

class Square(regularpolygon.RegularPolygon):
    def __init__(self, length):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length **2

if __name__ == '__main__':
    square = Square(10)
    print('square: ' + str(square.area))
```

In case you're wondering about `from . import regularpolygon`: While we could have used 

Now you can remove the old `polygons.py` file. An easy way to check that everything is still working is go try executing the `square.py` file.

```bash
(venv) 
polygons $ python polygons/square.py 
square: 100
(venv) 
polygons $ 
```

You can also confirm that the multi-file module works.

```python
(venv)
polygons $ python
>>> from polygons import regularpolygon
>>> print(regularpolygon.RegularPolygon(4, 5).area)
25.000000000000004
```

> Note: Huh. Not `25`? We'll fix that little bug a bit later.

Cleaning Up our Multi-File Module
---------------------------------

We've got a bit of ugliness with our first translation from module to multi-file module.

- `import polygons` no longer gives us access to the actual code we want.
- Getting access to the `RegularPolygon` or `Square` classes requires that we use `from polygon import <class>`.
- Creating instances of our `RegularPolygon and `Square` classes requires some needless reference to the individual module in which they reside.
- Using `from polygons import * ` should provide direct access to the `RegularPolygon` and `Square` classes.

We want to be able to say `import polygons` and immediately be able to do things like `square = polygons.Square(4)`, or `from polygons import square` and have `square = Square(4)` available to us. We accomplish this by giving `__init__.py` some content.

When we import a multi-file module, we're providing the name of the folder that contains the individual modules.

> REF: http://www.diveintopython3.net/packaging.html
> REF: http://docs.python-guide.org/en/latest/shipping/packaging/
> REF: http://docs.python-guide.org/en/latest/writing/structure/
> REF: http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html

[Next: Testing][1]

[1]: ch_04_testing.md 'Chapter 4: Testing'
[2]: https://en.wikipedia.org/wiki/Mark_Pilgrim 'Mark Pilgrim on Wikipedia'
[3]: http://www.diveintopython3.net/case-study-porting-chardet-to-python-3.html#multifile-modules 'A Short Digression Into Multi-File Modules'
