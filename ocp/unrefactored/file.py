import csv
from typing import List, Dict


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


    def read_csv_file(self, file_path: str) -> List:

        with open(file_path, "rt", encoding='iso-8859-1') as file:
            reader = csv.reader(file)

            for row in reader:
                self._set_data(
                    name=row[0].split(';')[0],
                    cpf=row[0].split(';')[1],
                    email=row[0].split(';')[2]
                )
        return self.data

    def read_txt_file(self, file_path: str) -> List:

        with open(file_path, "r") as file:
            for row in file:
                self._set_data(
                    cpf=row[0:11],
                    name=row[11:41].rstrip(),
                    email=row[41:80]
                )
        return self.data
