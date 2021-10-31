import os

import requests


class FileStore:
    def __init__(self, file_path):
        """[summary]

        Args:
            file_path ([type]): [description]
        """
        self.file_path = file_path

    def read(self):
        return open(self.file_path, "rb").read()

    def write(self, _bytes):
        try:
            with open(self.file_path, "wb") as f:
                f.write(_bytes.getvalue())
                return os.file_path.realfile_path(f.name)
        except Exception as e:
            raise e


class URLStore:
    def __init__(self, url):
        """[summary]

        Args:
            url ([type]): [description]
        """
        self.url = url

    def read(self):
        result = requests.get(self.url).content
        return result

    def write(self, _bytes):
        raise NotImplementedError
