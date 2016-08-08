A Simple Project
================

For this to be a tutorial, we're going to need an actual project with actual code that actually does something.  I've seen other tutorials of this sort work with `ModuleA` and `MyClass` with `a_function`, and Python is known for `spam` and `eggs`, which is fine, but I find such names to be difficult to follow.

So, after thinking for a bit about it, I decided to come up with as simple a project as I could that actually did something, perhaps even something useful, which is `polygons.py` (with thanks to [wikiHow][1] for the math behind the algorithm), the listing of which is found below.

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

class Square(RegularPolygon):
    def __init__(self, length):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length ** 2

hexagon = RegularPolygon(6, 10)
print('hexagon: ' + str(hexagon.area))

square = Square(10)
print('square: ' + str(square.area))
```

While the above code may seem trivial, I can see someone writing it if they needed to calculate regular polygon areas, well, regularly. And once the code is written (and tested, to be covered later), perhaps it would be useful to others, so we should package it up as a library. And so that one doesn't have to be a programmer to take advantage of it, create a command line utility and a GUI app using the library.

[Next: The Python Development Environment][2]

[1]: http://www.wikihow.com/Find-the-Area-of-Regular-Polygons "wikiHow's article on calculating the area of a regular polygon"
[2]: ch_02_the_python_dev_env.md 'Chapter 2: The Python Development Environment'
