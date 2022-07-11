from json import load, dump

from jsonpickle import encode, decode


class DataSerializer:
    def __init__(self, database):
        self._database = database

    def load_from_file(self):
        file = open(self._database.file.path)
        characters = load(file)
        self._database.characters.set(self._deserialize(characters))
        file.close()

    def save_to_file(self):
        file = open(self._database.file.path, 'w')
        dump(self._serialize(), file)
        file.close()

    def _serialize(self) -> list:
        characters = []

        for character in self._database.characters.get():
            characters.append(encode(character))

        return characters

    def _deserialize(self, characters_list_from_file: list) -> list:
        characters = []

        for character in characters_list_from_file:
            characters.append(decode(character))

        return characters
