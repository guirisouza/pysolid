from rectangle import Rectangle


class Square(Rectangle):

    def set_height(self, height: float) -> None:
        self.height = height
        self.width = height

    def set_width(self, width: float) -> None:
        self.width = width
        self.height = width
