from typing import List


class File:
    def __init__(self):
        self.data: List = []

    def _set_data(self, name: str, cpf: str, email: str) -> None:
        self.data.append(
            {
                "name": name,
                "cpf": cpf,
                "email": email
            }
        )

    def get_data(self):
        return self.data

    def read_file(self, file_path: str) -> List:
        pass
