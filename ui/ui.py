from system_messages import SystemMessages
from constants import Constants


class UserInterface:
    def get_user_input(self, msg: str = '') -> str:
        return input(msg)

    def print_message(self, msg: str):
        print(msg)

    def print_list(self, list: list):
        for item in list:
            print(item)

    def show_dialog(
            self,
            msg: str = '',
            error_msg: str = SystemMessages.Command_not_recognized,
            yes: str = Constants.YES_INPUT,
            no: str = Constants.NO_INPUT
        ):
        user_input = self.get_user_input(msg)
        if user_input == yes:
            return True
        elif user_input == no:
            return False
        else:
            self.print_message(error_msg)
            self.show_dialog(msg)
