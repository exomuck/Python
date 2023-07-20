import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            print("<class 'LengthException'> was raised")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def set_width(self, new_width):
        if new_width <= 0:
            print("<class '__main__.LengthException'> was raised")
        else:
            self.width = new_width

    def set_height(self, new_height):
        if new_height <= 0:
            print("<class '__main__.LengthException'> was raised")
        else:
            self.height = new_height