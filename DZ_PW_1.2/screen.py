from console import *
from colorama import Fore, Back, Style
from baseclasses import Abstract_view


""" 
|------------------------------------------|
|                   TITLE                  |
|------------------------------------------|
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |
|------------------------------------------|
|                  STATUS                  |
|------------------------------------------|
"""


class Screen(Abstract_view):
    """ Клас що описує сутність екран """

    def __init__(self, title: str, status: str) -> None:
        self.title = title.upper()
        self.status = status.upper()
        self.h, self.w = get_console_size()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def status(self, value):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def draw(self):
        self.h, self.w = get_console_size()
        clear_console()
        move_cursor(0, 0)
        print(Fore.GREEN+'|' + '-'*(self.w-2) + '|')
        print(Fore.GREEN+'|' + Fore.RED +
              self._title.center(self.w-2) + Fore.GREEN + '|')
        print(f'{Fore.GREEN}'+'|' + '-'*(self.w-2) + '|')

        for i in range(self.h-6-1):
            print(f'{Fore.GREEN}'+'|'+' '*(self.w-2)+'|')

        print(f'{Fore.GREEN}'+'|' + '-'*(self.w-2) + '|')
        print(Fore.GREEN+'|' + Fore.RED +
              self._status.center(self.w-2) + Fore.GREEN + '|')
        print(f'{Fore.GREEN}'+'|' + '-'*(self.w-2) + '|')
