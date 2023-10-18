from typing import Dict, List

from csv_file import CsvFile
from txt import Txt

class FileReader():
    def __init__(self):
        self._file: str = ""
        self._file_path: str = ""

    def get_file_path(self) -> str:
        return self._file_path

    def set_file_path(self, file_path: str) -> None:
        self._file_path = file_path

    def set_file(self, file: str) -> None:
        self._file = file

    def read_file(self) -> List:
        file_ext = self._file_path.split('.')[-1]

        return {
            "txt": Txt(),
            "csv": CsvFile()
        }.get(file_ext).read_file(file_path=self._file_path)




