from utils import help
from command import Command

from .abstract_action import Action


class HelpAction(Action):
    @property
    def bound_command(self) -> str:
        return Command.HELP

    def run(self):
        help()
