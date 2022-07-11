from ui import ui
from db import db
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class PrintDatabaseAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.PRINT_DATABASE

    def run(self):
        ui.print_message(db.file.current_db)
