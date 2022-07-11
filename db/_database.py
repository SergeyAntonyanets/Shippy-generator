from ._data_serializer import DataSerializer
from ._database_file_manager import DatabaseFileManager
from ._database_character_handler import DatabaseCharacterHandler


class Database:
    characters: DatabaseCharacterHandler
    file: DatabaseFileManager
    data: DataSerializer

    def __init__(self):
        self.characters = DatabaseCharacterHandler()
        self.file = DatabaseFileManager()
        self.data = DataSerializer(self)
