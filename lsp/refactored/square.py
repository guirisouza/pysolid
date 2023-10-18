

class Square:
    def __init__(self):
        self.height: float = 0
        self.width: float = 0

    def set_height(self, height: float) -> None:
        self.height = height
        self.width = height

    def set_width(self, width: float) -> None:
        self.width = width
        self.height = width

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
