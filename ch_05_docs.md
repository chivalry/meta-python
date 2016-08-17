Documentation
=============

"Documentation" can mean a few things in the Python community. At the simplest level, documentation can just be the [docstrings][2] included with your modules, classes, and functions. The next level up would probably be external user documentation files, probably written in [Markdown][3] or [reStructuredText][4], using a utility such as [Sphinx][5] to convert the original files into other formats such as HTML or PDF. These documentation files are the ones anyone who wants to use your library would reference. Finally, if you want other contributors to have specific information about assisting with development, you can include external developer documentation files, also written in some markup language and converted to various formats with `sphinx`.

Docstrings
----------

Even within the single format of docstrings, there are multiple ways to format the contents of the docstrings, such as [Epydoc][6] and [Google's Python Style Guide][7]. We'll be using the reStructuredText within our docstrings in order to allow Sphinx to automatically include them within the generated documentation files. We'll also be including some fairly superfluous docstrings, one for each multi-file module, module, class, and function, so that we can see exactly what Sphinx will do with them.

`polygons/__init__.py` becomes:

```python
"""Provides utilities for calculating polygon areas.
"""

from . import polygon
from . import regularpolygon

__all__ = ['polygon', 'regularpolygon']
```

`polygons/polygon/__init__.py`:

```python
"""Provides utilities for working with (irregular) polygons.
"""

from .polygon import Polygon
```

`polygons/polygon/polygon.py`:

```python
class Polygon:
    """A class representing any polygon as a list of sides and a list of angles.
    """

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
        """Initialize the Polygon class.

           :param sides: The number of sides the polygon has
           :param lengths: A list of lengths for each side
           :param angles: A list of angles, angle i is between lengths i and i + 1
           :raises ValueError: if arguments are invalid for any reason
        """
        self.sides = sides
        self.lengths = lengths
        self.angles = angles
        
        self.confirm_attributes()

    @property
    def perimeter(self) -> float:
        """Return the perimiter of the polygon.
        """
        return sum(self.lengths)

    @property
    def name(self) -> str:
        """Return the name of the polygon.
        """
        return self.names[self.sides]

    def confirm_attributes(self):
        """Confirm attributes are within bounds restrictions.
        """
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

`polygons/regularpolygon/__init__.py`:

```python
"""Provides utilities for calculating regular polygon areas.
"""

from .regularpolygon import RegularPolygon
from .square import Square
from .equilateraltriangle import EquilateralTriangle
```

`polygons/regularpolygon/regularpolygon.py`:

```python
import math
from ..polygon.polygon import Polygon

class RegularPolygon(Polygon):
    """A class representing any regular polygon.
    """

    def __init__(self, sides:int, length:float):
    """Initialize the RegularPolygon class.
    
       :param sides: The number of sides the regular polygon has
       :param length: The length of each side
       :raises ValueError: if sides or length are invalid values
    """
        self.length = length
        lengths = [length] * sides
        angles = [self.angle(sides)] * sides
        super().__init__(sides, lengths, angles)

    @property
    def perimeter(self) -> float:
        """Return the perimiter of the regular polygon.
        """
        return self.sides * self.length

    @property
    def apothem(self) -> float:
        """Return the apothem of the regular polygon.
        """
        tan = math.tan(math.pi / self.sides)
        return self.length / (2 * tan)

    @property
    def area(self) -> float:
        """Return the area of the regular polygon.
        """
        if self.sides == 4:
            return self.length ** 2
        else:
            return (self.apothem * self.perimeter) / 2

    @classmethod
    def angle(self, sides:int) -> float:
        """Return the calculated angle for a regular polygon with the given sides.

           :param sides: The number of sides of the regular polygon
           :raise ValueError: if sides < 3 or not an int
        """
        if sides < 3:
            raise ValueError('cannot calculate angles of polygon with less than 3 sides')
        elif type(sides) != int:
            raise ValueError('sides must be an int')
        angle_sum = 180 * (sides - 2)
        return angle_sum / sides
```

`polygons/regularpolygon/square.py`:

```python
from .regularpolygon import RegularPolygon

class Square(RegularPolygon):
    """A class to represent a square.
    """

    def __init__(self, length:float):
        """Initialize the Square class.
        """
        super().__init__(4, length)

    @property
    def area(self):
        """Return the area of the square.
        """
        return self.length ** 2

    @property
    def name(self):
        """Override `Polygon.name` function.
        """
        return 'square'
```

`polygons/regularpolygon/equilateraltriangle.py`:

```python
import math
from .regularpolygon import RegularPolygon

class EquilateralTriangle(RegularPolygon):
    """A class to represent an equilateral triangle.
    """

    def __init__(self, length:float):
        """Initialzie the EquilateralTriangle class.
        """
        super().__init__(3, length)

    @property
    def area(self) -> float:
        """Return the area of the equilateral triangle.
        """
        return (self.length ** 2) * math.sqrt(3) / 4

    @property
    def name(self) -> str:
        """Override Polygon.area function.
        """
        return 'equilateral triangle'
```

User Documentation
------------------

Developer Documentation
-----------------------

[Next: Distribution][1]

[1]: ch_06_dist.md 'Chapter 6: Distribution'
[2]: https://www.python.org/dev/peps/pep-0257/ 'PEP 257 — Docstring Conventions'
[3]: https://daringfireball.net/projects/markdown/ 'Markdown'
[4]: http://docutils.sourceforge.net/rst.html 'reStructuredText'
[5]: http://www.sphinx-doc.org/en/stable/ 'Sphinx'
[6]: http://epydoc.sourceforge.net/ 'Epidoc'
[7]: https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments "Google's Python Style Guide"

<!--
http://docs.python-guide.org/en/latest/writing/documentation/
https://www.youtube.com/watch?feature=player_embedded&v=oJsUvBQyHBs
-->
