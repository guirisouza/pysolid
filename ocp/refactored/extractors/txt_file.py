from typing import List

from ocp.refactored.file import File


class TxtFile(File):

    def read_file(self, file_path: str) -> List:

        with open(file_path, "r") as file:
            for row in file:
                self._set_data(
                    cpf=row[0:11],
                    name=row[11:41].rstrip(),
                    email=row[41:80]
                )
        return self.data