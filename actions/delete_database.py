from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class DeleteDatabaseAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.DELETE_DB_FILE

    def run(self):
        user_input = ui.get_user_input(
            'Введите имя базы данных, которая должна быть удалена.'
        )

        if db.file.is_file(user_input):
            result = ui.show_dialog(
                f'Вы действительно хотите удалить базу данных: {user_input}? {SystemMessages.YES_OR_NO_HINT}'
            )

            if result:
                db.file.delete(user_input)
                ui.print_message(SystemMessages.DATABASE_DELETED)
            else:
                ui.print_message(SystemMessages.CANCELED)
