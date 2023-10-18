from typing import List

from item import Item


class Cart:
    def __init__(self, items: List = []) -> None:
        self.items = items

    def get_items(self) -> List:
        return self.items

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def validate(self):
        return len(self.items) > 0