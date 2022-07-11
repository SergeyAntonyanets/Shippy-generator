class Character(object):
    _name: str

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    @property
    def name(self) -> str:
        return self._name
