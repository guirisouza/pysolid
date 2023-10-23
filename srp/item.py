

class Item:
    def __init__(self, description: str = "", value: float = 0) -> None:
        self.description: str = description
        self.value: float = value

    def __repr__(self):
        return  f"[{self.description} | {self.value}]"

    def __str__(self):
        return f"Nome: {self.description} | Valor: {self.value}"

    def validate(self):
        if self.value <= 0:
            return False
        if not self.description:
            return False
        return True

    def get_description(self) -> str:
        return self.description

    def get_value(self) -> float:
        return self.value

    def set_description(self, description: str) -> None:
        if not isinstance(description, str):
            print('Description must be an string')
            return
        self.description = description

    def set_value(self, value: float) -> None:
        if not isinstance(value, float):
            print('Value must be an float type')
            return
        self.value = value