from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_width):
        if new_width <= 0:
            print("<class '__main__.LengthException'> was raised")
        else:
            self.width = new_width
            self.height = new_width

    def set_height(self, new_height):
        if new_height <= 0:
            print("<class '__main__.LengthException'> was raised")
        else:
            self.width = new_height
            self.height = new_height