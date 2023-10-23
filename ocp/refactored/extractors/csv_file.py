import csv
from typing import List

from ocp.refactored.file import File


class CsvFile(File):
    def read_file(self, file_path: str) -> List:

        with open(file_path, "rt", encoding='iso-8859-1') as file:
            reader = csv.reader(file)

            for row in reader:
                self._set_data(
                    name=row[0].split(';')[0],
                    cpf=row[0].split(';')[1],
                    email=row[0].split(';')[2]
                )
        return self.get_data()