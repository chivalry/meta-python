A Simple Project
================

For this to be a tutorial, we're going to need an actual project with actual code that actually does something.  I've seen other tutorials of this sort work with `ModuleA` and `MyClass` with `a_function`, and Python is known for `spam` and `eggs`, which is fine, but I find such names to be difficult to follow.

So, after thinking for a bit about it, I decided to come up with as simple a project as I could that actually did something, perhaps even something useful, which is `polygons.py` (with thanks to [wikiHow][1] for the math behind the algorithms), the listing of which is found below.

```python
import math

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

    @property
    def perimeter(self):
        return sum(self.lengths)

    @property
    def name(self):
        return self.names[self.sides]

class RegularPolygon(Polygon):
    def __init__(self, sides:int, length:float):
        self.length = length
        lengths = [length] * sides
        angles = [RegularPolygon.angle(sides)] * sides
        super().__init__(sides, lengths, angles)

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

    @classmethod
    def angle(self, sides):
        angle_sum = 180 * (sides - 2)
        return angle_sum / sides

class Square(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length ** 2

    @property
    def name(self):
        return 'square'

class EquilateralTriangle(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return (self.length ** 2) * math.sqrt(3) / 4

    @property
    def name(self):
        return 'equilateral triangle'

hexagon = RegularPolygon(6, 10)
print('hexagon area: ' + str(hexagon.area))
print('hexagon name: ' + hexagon.name)
print('hexagon angles: ' + str(hexagon.angles))

square = Square(10)
print('square area: ' + str(square.area))

triangle = EquilateralTriangle(9)
print('triangle area: ' + str(triangle.area))
```

While the above code may seem trivial, I can see someone writing it if they needed to calculate regular polygon areas, well, regularly, and it's complicated enough that we'll be able to use it to create a multi-file module (i.e., package) with sub-modules.. And once the code is written (and tested, to be covered later), perhaps it would be useful to others, so we should package it up as a library. And so that one doesn't have to be a programmer to take advantage of it, create a command line utility and a GUI app using the library.

[Next: The Python Development Environment][2]

[1]: http://www.wikihow.com/Find-the-Area-of-Regular-Polygons "wikiHow's article on calculating the area of a regular polygon"
[2]: ch_02_the_python_dev_env.md 'Chapter 2: The Python Development Environment'
