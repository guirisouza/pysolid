from typing import List


class Cart:
    def __init__(self, status: str = "aberto", items: List = []) -> None:
        self.items = items
        self.status = status
        self.total_value = 0

    def get_items(self) -> List:
        return self.items

    def add_item(self, item: str, value: float):
        self.items.append({"name": item, "value": value})
        self.total_value += value

    def get_total_value(self) -> float:
        return self.total_value

    def get_status(self) -> str:
        return self.status

    def confirm_order(self):
        if self.validate_cart():
            self.status = "confirmado"
            self.send_confirm_email()
            return True

        print("não há nenhum pedido")
        return False

    def send_confirm_email(self):
        print('...email enviado: pedido confirmado')

    def validate_cart(self) -> bool:
        return len(self.items) > 0
