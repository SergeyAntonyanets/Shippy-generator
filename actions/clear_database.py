from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class ClearDatabaseAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.CLEAR_DATABASE

    def run(self):
        result = ui.show_dialog(
            f'Вы действительно хотите очистить базу данных? {SystemMessages.YES_OR_NO_HINT}'
        )

        if result:
            db.characters.clear()
            db.data.save_to_file()
            ui.print_message(SystemMessages.DATABASE_CLEARD)
        else:
            ui.print_message(SystemMessages.CANCELED)
