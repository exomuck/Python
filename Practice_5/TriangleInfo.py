import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            print("<class 'LengthException'> was raised")
        elif a + b <= c or b + c <= a or c + a <= b:
            print("<class 'InvalidTriangleException'> was raised")
        else:
            self.a = a
            self.b = b
            self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_height_a(self):
        return 2 * self.area() / self.a

    def get_height_b(self):
        return 2 * self.area() / self.b

    def get_height_c(self):
        return 2 * self.area() / self.c