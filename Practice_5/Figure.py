import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            print("<class '__main__.LengthException'> was raised")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            print("<class '__main__.LengthException'> was raised")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            print("<class '__main__.LengthException'> was raised")
        elif a + b <= c or b + c <= a or c + a <= b:
            print("<class '__main__.InvalidTriangleException'> was raised")
        else:
            self.a = a
            self.b = b
            self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


rec = Rectangle(-1, 2)
tri = Triangle(3, 4, 7)

rec = Rectangle(1, 2)
tri = Triangle(3, 4, 5)
print(rec.perimeter())
print(tri.area())