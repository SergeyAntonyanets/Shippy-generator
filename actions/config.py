from .help import HelpAction
from .print_all_characters import PrintAllCharactersAction
from .delete_character import DeleteCharacterAction
from .add_character import AddCharacterAction
from.print_all_databases import PrintAllDatabasesAction
from .print_database import PrintDatabaseAction
from .change_database_file import ChangeDatabaseFileAction
from .create_database import CreateDatabaseAction
from .clear_database import ClearDatabaseAction
from .exit import ExitAction
from .generate import GenerateAction
from .delete_database import DeleteDatabaseAction

action_list = [
    ExitAction(),
    GenerateAction(),
    CreateDatabaseAction(),
    DeleteDatabaseAction(),
    ClearDatabaseAction(),
    ChangeDatabaseFileAction(),
    PrintDatabaseAction(),
    PrintAllDatabasesAction(),
    AddCharacterAction(),
    DeleteCharacterAction(),
    PrintAllCharactersAction(),
    HelpAction(),
]
