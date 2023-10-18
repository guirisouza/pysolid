from typing import Union
from rectangle import Rectangle
from square import Square

class Polygon:
    def __init__(self):
        self.form: Union[Square|Rectangle|None] = None

    def get_form(self):
        return self.form

    def set_form(self, form: object) -> None:
        self.form = form

    def get_area(self):
        return self.form.get_width() * self.form.get_height()