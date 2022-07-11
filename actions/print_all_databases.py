from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class PrintAllDatabasesAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.PRINT_ALL_DATABASES

    def run(self):
        if len(db.file.all_dbs) > 0:
            ui.print_message('Существующие базы данных:')
            ui.print_list(db.file.all_dbs)
        else:
            ui.print_message('Нет баз данных')
