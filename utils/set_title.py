from os import system

from constants import Constants


def set_title():
    system(f'title {Constants.APPLICATION_TITLE}')
