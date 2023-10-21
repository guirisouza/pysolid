from typing import List, Dict


class Cart:
    def __init__(self, status: str = "open", items: List[Dict] = []) -> None:
        self.items: List = items
        self.status: str = status
        self.total_value: float = 0

    def add_item(self, item: str, value: float) -> None:
        self.items.append({"name": item, "value": value})
        self.total_value += value

    def get_items(self) -> List:
        return self.items

    def validate_item(self, item: dict) -> bool:
        if not item.get('name') or not item.get('value'):
            return False
        if item.get('value') <= 0:
            return False
        return True

    def get_total_value(self) -> float:
        return self.total_value

    def get_status(self) -> str:
        return self.status

    def confirm_order(self):
        if self.validate():
            self.status = "confirmed"
            self.send_confirm_email()

        print("There are no items in the cart")
        return False

    def send_confirm_email(self):
        print('...Email Sent: order confirmed')

    def validate(self) -> bool:
        return len(self.items) > 0
