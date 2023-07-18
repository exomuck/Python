class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"<Width = {self.width}, Height = {self.height}>"""

# Test case:
a = Rect(4, 5)
print(a)
print(a.area(), a.perimeter())