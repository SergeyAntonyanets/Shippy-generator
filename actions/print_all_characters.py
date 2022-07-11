from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class PrintAllCharactersAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.PRINT_ALLCHARACTERS_IN_DATABASE

    def run(self):
        if len(db.characters.get()) > 0:
            ui.print_message('Персонажы в базе данных:')
            ui.print_list(db.characters.get())
        else:
            ui.print_message('База данных пуста')
