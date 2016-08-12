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

> Note: Even if you're on macOS, your shell prompt may look a bit different from mine. I've customized by shell prompt to insert a blank line after each command as I find it easier to read. In case you're interested in how I did this, I have the following line in `~/.bash_profile`: `PS1="\n\W \$ "`. Once the virtual environment is activated, it temporarily edits the prompt to place the name of the virtual environment before the default prompt, so that while the virtual environment is active, `echo $PS1` returns `(venv) \n\w $ ` (`echo`ing the variable doesn't escape the `$`). This only happens for the current shell instance (so you won't see the different prompt if you create a new shell) and until you `deactivate` the virtual environment or close the current session.

<!-- separate block quotes -->
> Tip: Actually, I lied. My default shell prompt is `\n\[\e[34m\]\W\[\e[m\] \$`. Those ugly codes colorize the working directory name to a dark blue, making it even easier to separate each command in the window. I used [EzPrompt][4] to help me figure out what those codes should be.

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

We're going to need to do some design work here. Our existing module has four classes: `Polygon`, `RegularPolygon` (which inherits from `Polygon`), `Square` and `EquilateralTriangle` (both of which inherit from `RegularPolygon`). While there are many ways we could break this up into a multi-file module, our goal will be to make the main parent module `polygons` (plural), with two submodules, `polygon` and `regularpolygon`. We'll place the `Polygon` class in the `polygon` module and the rest in the `regularpolgon` module. Our structure will therefore be something like this.

```
polygons
    polygon
        polygon.py
    regularpolygon
        regularpolygon.py
        square.py
        equilateraltriangle.py
```

But, remember, a multi-file module needs to have a `__init__.py` file, and since we have one parent module and two sub-modules, we'll need three different `__init__.py` files.

```
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
```

If, within our project directory we create this folder structure, with blank `__init__.py` files and each of the other files containing their class definitions (with appropriate imports as needed), we have officially created a multi-file module.

Create the above directory and file structure within the existing `polygons` folder and transfer the various class definitions into the appropriate files. We'll get to what each class file needs for `include`s in a moment.

Note that you'll end up with a `polygons` folder *inside* the existing `polygons` folder. The top one will be the " published Python library available for easy installation and use" package folder, the inside one the "directory of modules that also contains a `__init__.py` file" package folder, our multi-file module with sub-modules. The final directory structure will look like this (excluding various utility directories, such as `venv`).

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
```

Now let's cover the what our four new files need in `include`s in order to work. `polygon.py` doesn't need anything. Our original `polygons.py` file only had one `include` for the `math` library, and the `polygon.py` file doesn't need that.

Both `regularpolygon.py` and `equilateraltriangle.py` need the `math` library, the first for `tan` and `pi`, the second for `sqrt`. Go ahead and add `import math` to the top of both of them.

But now we need to think things through a bit. The `RegularPolygon` class inherits from `Polygon` and both `Square` and `EquilateralTriangle` inherit from `RegularPolygon`, but these files span two folders, so how do we tell the `regularpolygon.py` file where to find the `Polygon` class?

Python uses a system similar to shell directory structures to indicate the current and parent modules. Just as `.` means the current directory and `..` means the parent directory within a command line shell, Python's import mechanism uses `.` to mean the current module and `..` the parent module. This dot notation is called the "relative namespace."

We have three modules: `polygons` (plural), `polygon` (singular), and `regularpolygon`, the latter two being sub-modules of the first, which is another way of saying that the first is the parent module of the latter two. So to navigate from the `regularpolygon` file to the `Polygon` class, we need to go up one module, then down into the `polygon` module, then into the `polygon` file/module. Add this below your `import math` in `regularpolygon.py`:

```python
from ..polygon.polygon import Polygon
```

You do not *have* to use relative namespaces. We could have used `from polygons.polygon.polygon import Polygon`, but doing so makes the structure more fragile. Should you ever decide later that the top-level module should be named something other than `polygons`, you'd then need to change all of the internal references to it that you've hardcoded.

Similarly, both the `Square` and `EquilateralTriangle` classes inherit from `RegularPolygon`, which is in the `regularpolygon.py` file. In this case we go to the *current* module (indicated by a `.`), and from there into the `regularpolygon` module/file. Add this line to both `square.py` and `equilateraltriangle.py`:

```python
from .regularpolygon import RegularPolygon
```

Note that we could have used `from . import regularpolygon.RegularPolygon`, but we would have to have then changed our class definition to inherit from `regularpolygon.RegularPolygon`, as in `class Square(regularpolygon.RegularPolygon)`. With the way we've done it we were able to copy and paste the code from our original file.

At this point we don't need our original `polygons.py` file. All of the code that was originally in it has been moved to our four class files. So go ahead and delete it, but there is one feature that file gave us which we no longer have.

Our assumption at this point is that we started with a Python script that we found useful and are moving toward publishing it on PyPI. Such small scripts often don't have testing built in other than what I showed with `if __name__…`. Eventually we'll add test suites to this, but in the meantime it would be nice to have a script that will load the new multi-file module and just output some printouts like our original did.

Create a `test.py` in our top-level `polygons` folder (i.e., at the same level `polygons.py` used to be) and give it the following content.

```python
from polygons.polygon.polygon import Polygon
from polygons.regularpolygon.regularpolygon import RegularPolygon
from polygons.regularpolygon.square import Square
from polygons.regularpolygon.equilateraltriangle import EquilateralTriangle

poly = Polygon(5, [3, 4, 5, 4, 6], [100, 110, 120, 130, 80])
print('poly name: ' + poly.name)
print('poly perimiter: ' + str(poly.perimeter))

hexagon = RegularPolygon(6, 10)
print('hexagon area: ' + str(hexagon.area))
print('hexagon name: ' + hexagon.name)
print('hexagon angles: ' + str(hexagon.angles))

print('square area: ' + str(Square(10).area))

print('triangle area: ' + str(EquilateralTriangle(9).area))
```

You may wonder why I didn't place these tests within each file's `if __name__…` block as I did with the original script. The reason is the relative namespaces we used above. Relative namespace only work when a file within a larger multi-file module is executed directly. Go ahead and try entering something like `python polygons/regularpolygon/square.py`. You'll get an import error because we're not using that file as part of the larger multi-file module and therefore the relative namespace won't work.

We now have a complete multi-file module which our `test.py` file confirms works to give us the same functionality as our original script, but those `import`s sure are ugly. Let's take care of that next.

Cleaning Up the Interface
=========================

I've repeatedly read that leaving `__init__.py` blank is a standard practice, and one can get things to work programmatically by doing so, but I consider the default interface into the module to be ugly, and the only way to get around that is to place some code in our various `__init__.py` files. The `import`s that navigate the module path above (i.e., `from polygons.polygon.polygon import Polygon`) are rather difficult to read and prone to error when typing. Ideally we'd like our module to have the following features:

- `import polygons` gives us access to all of the submodules with their classes.
- `import polygons` also allows us to refer to the classes by `module.submodule.Class`, without the extra reference to the file.
- `from polygons import *` gives access to the classes with `submodule.Class`.
- If we only need access to a single class, we can use something like `from polygons.polygon import Polygon`.

What most of these actually have in common is the elimination of the filenames in the module paths. The exception is the ability to import all of the module's namespace. But all of this is accomplished by adding some code to the `__init__.py` files.

While the presence of `__init__.py` within a folder does flag that folder as a module, any code that is in the file will get executed when the module gets imported.

Try this: Edit the existing `polygons/__init__.py` to just have a line that says, `print('Hello from __init__.py')`. Then enter the Python interpreter and type `import polygons`.

```
>>> import polygons
Hello from __init__.py
>>> 
```

If you followed the above experiment, remove the line from `polygons/__init__.py`. We're going to go from the inside out with with, starting with our `polygons.polygon` module. Edit `polygons/polygon/__init__.py` to have a single line:

```python
from .polygon import Polygon
```

This line says, "When loading the `polygon` module (because the line is in `polygons/polygon/__init__.py`), within that module look for a submodule called `polygon` (which it will find because this folder contains the file `polygon.py`) and load the `Polygon` name from it." The net effect is that when the `polygon` submodule is loaded, we bypass the filename of the `Polygon` class when referencing it.

You can probably guess the contents of `polygons/regularpolygon/__init__.py`, but here it is for reference sake:

```python
from .regularpolygon import RegularPolygon
from .square import Square
from .equilateraltriangle import EquilateralTriangle
```

Moving up one level, we turn to `polygons/__init__.py`. Our first order of business will be to make it such that loading the `polygons` parent module automatically also loads the two submodules, which is done with the following:

```python
from . import polygon
from . import regularpolygon
```

In English, the first lines says, "When loading the `polygons` module (because this code is within `polygons/__init__.py`) load the `polygon` submodule (in this case, a folder with its own `__init__.py` file)."

At this point you could enter the Python interpreter and get immediate access to the entire module with `import polygons` and gain easier syntactical access.

```
>>> import polygons
>>> s = polygons.regularpolygon.Square(13)
>>> print(s.perimeter)
52
>>>
```

We've now only one goal remaining to make the interface into our module easier. Although it's officially discouraged, developers expect something like `from polygons import *` to work, and at this point it won't, or at least not quite how we would expect.

If you again enter the Python interpreter and enter `from polygons import *`, you will get access to all of the classes, but you'll need to reference their full module path, as in `s = polygons.regularpolygon.Square(9)`. What we want is for `from polygons import *` to remove that top level, so we can say something like `s = regularpolygon.Square(9)`. This is accomplished with the `__all__` variable, which specifies which submodules should be imported when the user requests, well, all of them. Add the following line to `polygons/__init__.py`:

```python
__all__ = ['polygon', 'regularpolygon']
```

Our English translation would be, "When the entire namespace of this module is requested, load the `polygon` and `regularpolygon` modules." Opening our Python interpreter will confirm that this is working.

```
>>> from polygons import *
>>> s = regularpolygon.Square(10)
>>> print(s.area)
100
>>>
```

Alternative Paths
=================

There are other ways we could have organized our multi-file module to make things easier from the interface point of view. We have a separate file for each of our classes, which actually means we have modules three levels deep. Each of the lines below is a module:

```
polygons
    polygon
        polygon.py
    regularpolygon
        equilateraltriangle.py
        regularpolygon.py
        square.py
```

Remember, a `.py` file is also a module, which is why our setup before we cleaned up the interface required module paths like `polygons.polygon.polygon.Polygon`.

One way we could have fixed this would be the have a shallower structure.

```
polygons
    polygon.py
    regularpolygon.py
```

`polygon.py` would contain the `Polygon` class and `regularpolygon.py` would contain the three other classes, allowing, without the imports we placed in our various `__init__.py` files, module paths like `polygons.polygon.Polygon`, which is where we ended up with in the other structure.

The reason I made things a bit harder on us is that, for larger multi-file modules, it's going to make organizational sense for us to break our classes into individual files. For something as small as this, we could safely combine multiple classes into a single file, but if we hadn't gone through this exercise of breaking them up, we wouldn't have learned as deeply and wouldn't be prepared for more complicated modules.

[Next: Testing][1]

[1]: ch_04_testing.md 'Chapter 4: Testing'
[2]: https://en.wikipedia.org/wiki/Mark_Pilgrim 'Mark Pilgrim on Wikipedia'
[3]: http://www.diveintopython3.net/case-study-porting-chardet-to-python-3.html#multifile-modules 'A Short Digression Into Multi-File Modules'
[4]: http://ezprompt.net/ 'EzPrompt'

<!--
REF: http://www.diveintopython3.net/packaging.html
REF: http://docs.python-guide.org/en/latest/shipping/packaging/
REF: http://docs.python-guide.org/en/latest/writing/structure/
REF: http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
-->
