from abc import ABC, abstractmethod, abstractproperty


class Action(ABC):
    @abstractproperty
    def bound_command(self) -> str:
        pass

    @property
    def execution_result(self) -> bool:
        return True

    @abstractmethod
    def run(self):
        pass
