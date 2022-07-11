from ui import ui
from db import db
from utils import generate_random_characters
from command import Command
from system_messages import SystemMessages

from .abstract_action import Action


class GenerateAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.GENERATE_RANDOM_CHARACTERS

    def run(self):
        characters = generate_random_characters(db.characters.get())

        if characters:
            ui.print_message(msg='Ваши персонажы:')
            ui.print_list(characters)
        else:
            ui.print_message(msg='В базе данных не достаточно имён для генерации!')
