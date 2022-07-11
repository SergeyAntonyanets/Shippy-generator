from pickle import dump, load

from command import Command

content = f'''
Как играть?

Для начала Вы должны выбрать базу данных, из которой будут загружаться персонажы. для этого введите команду {Command.CHANGE_DB_FILE}.
Эту команду можно использовать напротяжении всей игры, чтобы выбирать разные базы данных.
Если баз данных нет, Вы должны будете создать новую. Чтобы это сделать, введите {Command.CREATE_DB_FILE} и следуйте инструкциям.
Когда закончите, Появится возможность добавить в базу своих персонажей. Введите {Command.ADD_CHARACTER} и следуйте инструкциям.
Если Вам понадобится удалить персонажа из базы, используйте {Command.DELETE_CHARACTER}.
После этого можно приступать к самой игре. Для генерации пяти рандомных персонажей введите {Command.GENERATE_RANDOM_CHARACTERS}.

Чтобы просмотреть все базы данных, используйте {Command.PRINT_ALL_DATABASES}.
Напротив выбранной базы будет знак *.
Если Вам нужно просто узнать, какую базу данных Вы используете, введите {Command.PRINT_DATABASE}.
А чтобы распичатать всех персонажей из базы, используйте команду {Command.PRINT_ALLCHARACTERS_IN_DATABASE}.

Если Вы захотите очистить или удалить базу данных, используйте команды {Command.CLEAR_DATABASE} и {Command.DELETE_DB_FILE} соответственно.

Приятной игры!!!
'''

file = open('h.pkl', 'wb')
dump(content, file)
file.close()