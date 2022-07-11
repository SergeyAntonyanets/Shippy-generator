from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class AddCharacterAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.ADD_CHARACTER

    def run(self):
        run = True

        while run:
            user_input = ui.get_user_input(
                f'Введите имя персонажа для сохранения в базе данных. {SystemMessages.STOP_ACTION_HINT}'
            )
            if user_input == Command.EMPTY_STRING:
                run = False
            else:
                db.characters.add(user_input)
