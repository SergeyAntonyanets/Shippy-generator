from ui import ui
from system_messages import SystemMessages
from actions.abstract_action import Action


class CommandHandler:
    _actions: list[Action]
    _command: str

    def __init__(self, actions: list[Action]):
        self._actions = actions

    def continue_execution(self) -> bool:
        result = self._process()
        return result

    def get_command(self, command: str):
        self._command = command

    def _process(self) -> bool:
        for action in self._actions:
            if action.bound_command == self._command:
                action.run()
                return action.execution_result
        ui.print_message(
            f'{SystemMessages.Command_not_recognized} {SystemMessages.HELP_HINT}'
        )

        return True
