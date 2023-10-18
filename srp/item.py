

class Item:
    def __init__(self, description: str = "", value: float = 0):
        self.description = description
        self.value = value

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

    def set_description(self, description: str) -> bool:
        if not isinstance(description, str):
            print('o nome do item precisa ser string')
            return False
        if len(description) < 4:
            print('item deve ser maior que 4 letras')
            return False
        self.description = description
        return True

    def set_value(self, value: float) -> bool:
        if not isinstance(value, float):
            return False
        self.value = value
        return True