

class Rectangle:
    def __init__(self):
        self.height: float = 0
        self.width: float = 0

    def set_height(self, height: float) -> None:
        self.height = height

    def set_width(self, width: float) -> None:
        self.width = width

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

