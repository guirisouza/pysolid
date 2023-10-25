from typing import List
import importlib
import inspect

from ocp.refactored.file import File


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

    def _import_extractor_by_file_extension(self, file_ext: str) -> File:
        extractor_module = importlib.import_module(f'extractors.{file_ext}_file')
        classes = inspect.getmembers(extractor_module, inspect.isclass)

        extractor = None

        for cls in classes:
            if cls[0] == f"{file_ext.title()}File":
                extractor = cls[1]()

        return extractor

    def read_file(self) -> List:
        file_ext = self._file_path.split('.')[-1]
        extractor_file = self._import_extractor_by_file_extension(file_ext=file_ext)

        return extractor_file.read_file(file_path=self._file_path)
