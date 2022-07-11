from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class DeleteCharacterAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.DELETE_CHARACTER

    def run(self):
        run = True

        while run:
            user_input = ui.get_user_input(
                f'Введите имя персонажа для удаления. {SystemMessages.STOP_ACTION_HINT}'
            )

            if user_input == Command.EMPTY_STRING:
                run = False
            else:
                result = db.characters.delete(user_input)

                if result:
                    ui.print_message(SystemMessages.CHARACTER_CREATED)
                else:
                    ui.print_message(
                        f'{SystemMessages.CHARACTER_NOT_FOUND} Убедитесь, что Вы правильно написали имя.'
                    )
