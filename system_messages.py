from command import Command


class SystemMessages:
    YES_OR_NO_HINT = 'Введите y для продолжения или n для отмены.'
    HELP_HINT = f'Для получения справки введите {Command.HELP}'
    STOP_ACTION_HINT = 'Когда закончите, нажмите enter.'
    CANCELED = 'Отменено'
    ENTER_A_COMMAND = 'Введите команду'
    Command_not_recognized = 'Команда не распознана!'
    CHARACTER_CREATED = 'Персонаж создан'
    CHARACTER_NOT_FOUND = 'Такого персонажа нет в базе данных!'
    DATABASE_NOT_FOUND = 'Такой базы данных не существует!'
    DATABASE_EXISTS = 'Такая база данных уже существует!'
    DATABASE_CHANGED = 'База данных изменена'
    DATABASE_CREATED = 'База данных создана'
    DATABASE_CLEARD = 'База данных очищена'
    DATABASE_DELETED = 'База данных удалена'
