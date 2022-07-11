from character import Character


class DatabaseCharacterHandler:
    _characters: list[Character]

    def __init__(self):
        self._characters = []

    def get(self) -> list[Character]:
        return self._characters

    def set(self, characters: list[Character]):
        self._characters = characters

    def add(self, name: str):
        self._characters.append(Character(name))

    def delete(self, name: str) -> bool:
        for character in self._characters:
            if character.name == name:
                self._characters.remove(character)
                return True
        return False

    def clear(self):
        self._characters.clear()
