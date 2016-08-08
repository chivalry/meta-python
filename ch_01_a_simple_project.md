For this to be a tutorial, we're going to need an actual project with actual code that actually does something.  I've seen other tutorials of this sort work with `ModuleA` and `MyClass` with `a_function`, which is fine, but I find such names to be difficult to follow.

So, after thinking for a bit about it, I decided to come up with as simple a project as I could that actually did something, perhaps even something useful, which is `polygons.py` (with thanks to [wikiHow](http://www.wikihow.com/Find-the-Area-of-Regular-Polygons) for the math behind the algorithm), the listing of which is found below.

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

Yes, it's fairly trivial, but we have something that at least looks like a real project, and it's something we can test, which will be useful later. The idea will be similar to what I was planning with the comic book archive library/command line tool/GUI app. We have some code here that performs a needed result, in this case, calculating the area of a regular polygon. We'll first translate that into a library that anyone else could use on PyPI. Then we'll create a command line tool and a GUI app, both of which will use that library.
