from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class CreateDatabaseAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.CREATE_DB_FILE

    def run(self):
        user_input = ui.get_user_input(msg='Введите имя новой базы данных')
        if not db.file.is_file(user_input):
            db.file.change(user_input)
            db.file.create()
            ui.print_message(msg=SystemMessages.DATABASE_CREATED)
        else:
            result = ui.show_dialog(
                f'{SystemMessages.DATABASE_EXISTS} {SystemMessages.YES_OR_NO_HINT}'
            )

            if result:
                db.file.change(user_input)
                db.file.create()
                ui.print_message(msg='База данных перезаписана')
            else:
                ui.print_message(SystemMessages.CANCELED)
