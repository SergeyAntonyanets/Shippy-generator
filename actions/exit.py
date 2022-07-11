from db import db
from command import Command

from .abstract_action import Action


class ExitAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.EXIT

    @property
    def execution_result(self) -> bool:
        return False

    def run(self):
        db.data.save_to_file()
