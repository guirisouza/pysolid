from cart import Cart

class Order:
    def __init__(self, cart: Cart, status: str = "aberto",):
        self.cart = cart
        self.status = status

    def get_cart(self) -> Cart:
        return self.cart

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status

    def confirm(self):
        if self.cart.validate():
            self.set_status(status='confirmado')
            return True
        return False