from file import File

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

    def get_file(self) -> str:
        file_ext = self._file_path.split('.')[-1]
        file = ""
        if file_ext == 'csv':
            file = File().read_csv_file(file_path=self._file_path)
        elif file_ext == 'txt':
            file = File().read_txt_file(file_path=self._file_path)
        return file

