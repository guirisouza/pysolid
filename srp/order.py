from cart import Cart
from email_service import EmailService

class Order:
    def __init__(self, cart: Cart, status: str = "open"):
        self.cart: Cart = cart
        self.status: str = status

    def get_cart(self) -> Cart:
        return self.cart

    def get_status(self) -> str:
        return self.status

    def set_status(self, status: str) -> None:
        self.status = status

    def confirm(self) -> bool:
        if self.cart.validate():
            self.set_status(status='confirmed')
            EmailService.send(
                subject="Order Confirmed",
                content="Dear, cliente. Your order was confirmed"
            )
            return True
        return False