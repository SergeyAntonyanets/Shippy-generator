from pickle import load
from os import system

from ui import ui
from command import Command
from constants import Constants
from system_messages import SystemMessages


def help():
    run = True

    system('cls')
    help_info = load_info_from_file(Constants.HELP_FILE)
    ui.print_message(SystemMessages.STOP_ACTION_HINT)
    ui.print_message(help_info)
    while run:
        user_input = ui.get_user_input()

        if user_input == Command.EMPTY_STRING:
            run = False


def load_info_from_file(file_name) -> str:
    file = open(file_name, 'rb')
    content = load(file)
    file.close()
    return content
