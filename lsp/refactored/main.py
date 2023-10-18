from polygon import Polygon
from square import Square
from rectangle import Rectangle

polygon = Polygon()
polygon.set_form(form=Square())
polygon.form.set_width(3)
polygon.form.set_height(4)
print(polygon.get_area())


polygon = Polygon()
polygon.set_form(form=Rectangle())
polygon.form.set_width(3)
polygon.form.set_height(4)
print(polygon.get_area())