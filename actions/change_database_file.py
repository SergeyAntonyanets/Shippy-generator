from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class ChangeDatabaseFileAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.CHANGE_DB_FILE

    def run(self):
        user_input = ui.get_user_input('Введите имя базы данных')
        if db.file.is_file(user_input):
            db.characters.clear()
            db.file.change(user_input)
            db.data.load_from_file()
            ui.print_message(SystemMessages.DATABASE_CHANGED)
        else:
            result = ui.show_dialog(
                f'{SystemMessages.DATABASE_NOT_FOUND}. Хотите создать новую? {SystemMessages.YES_OR_NO_HINT}'
            )
            if result:
                db.file.create(user_input)
                ui.print_message(SystemMessages.DATABASE_CREATED)
            else:
                ui.print_message(SystemMessages.CANCELED)
