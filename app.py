import sys

from command_handler import CommandHandler
from actions.config import action_list
from db import db
from utils import set_title
from ui import ui
from system_messages import SystemMessages


class App:
    _run: bool = True
    _command_handler = CommandHandler(action_list)

    def __init__(self):
        set_title()
        db.data.load_from_file()
        ui.print_message(SystemMessages.HELP_HINT)

    def run(self):
        while self._run:
            user_input = ui.get_user_input(SystemMessages.ENTER_A_COMMAND)
            self._command_handler.get_command(user_input)
            self._run = self._command_handler.continue_execution()
        sys.exit()
