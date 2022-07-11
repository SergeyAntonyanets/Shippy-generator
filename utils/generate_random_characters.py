from random import choice


def generate_random_characters(characters: list) -> list:
    returned_characters = []

    if len(characters) > 5:
        while len(returned_characters) < 5:
            character = choice(characters)
            if not character in returned_characters:
                returned_characters.append(character)
    elif len(characters) == 5:
        returned_characters = characters
    return returned_characters
