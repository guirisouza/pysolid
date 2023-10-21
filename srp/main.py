from item import Item
from cart import Cart
from order import Order

cart: Cart = Cart()
order: Order = Order(cart=cart)

item1: Item = Item()
item2: Item = Item()

item1.set_description(description='Wooden Chair')
item1.set_value(value=50)

item2.set_description(description='LED Lamp')
item2.set_value(value=14)

order.cart.add_item(item1)
order.cart.add_item(item2)

print(order.cart.get_items())
print(order.get_status())
print(order.cart.validate())
print(order.confirm())
print(order.get_status())