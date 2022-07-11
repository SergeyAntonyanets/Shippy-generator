from os import mkdir, remove, listdir
from os.path import isdir, isfile


class DatabaseFileManager:
    _file_name: str
    _file_type: str
    _folder: str

    def __init__(self):
        self._folder = 'dbs'
        self._file_type = 'json'
        self._file_name = 'default'

        self.check_folder()
        self.check_file()

    @property
    def path(self) -> str:
        return f'{self._folder}/{self._file_name}.{self._file_type}'

    @property
    def current_db(self) -> str:
        return self._file_name

    @property
    def all_dbs(self) -> list:
        all_databases = []
        for db in listdir(self._folder):
            if db in f'{self._file_name}.{self._file_type}':
                all_databases.append(f'*{db}'.removesuffix(self._file_type))
            else:
                all_databases.append(db.removesuffix(self._file_type))
        return all_databases

    def is_file(self, file_name: str) -> bool:
        if not isfile(f'{self._folder}/{file_name}.{self._file_type}'):
            return False
        return True

    def check_folder(self):
        if not isdir(self._folder):
            mkdir(self._folder)

    def check_file(self):
        if not isfile(self.path):
            self.create()

    def create(self, file_name: str = None):
        if file_name is not None:
            self.change(file_name)

        file = open(self.path, 'w', encoding='utf8')
        file.write('[]')
        file.close()

    def delete(self, file_name: str = None):
        remove(f'{self._folder}/{file_name}.{self._file_type}')

    def change(self, file_name: str):
        self._file_name = file_name
