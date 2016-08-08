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
