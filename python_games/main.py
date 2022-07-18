from typing import List, ClassVar

import game_number_guessing
import game_hangman
import game_twenty_one

from constants import read_a_text_file, input_of_the_variable, \
                      call_the_game_list


class PythonGames:
    def __init__(self) -> None:
        self.__game_list: List[str] = self.__read_game_list()
        self.__game: int = self.__input_of_the_game()
        self.__start_the_game()

    @staticmethod
    def __read_game_list() -> List[str]:
        return read_a_text_file('game_list.txt')

    def __header(self) -> None:
        print('GAME LIST')
        for game in self.__game_list:
            print(game)

    def __input_of_the_game(self) -> int:
        self.__header()
        return input_of_the_variable('Choose the game: ', f'Error! Choose one'
                                     f' of {len(self.__game_list)} games.',
                                     len(self.__game_list))

    def __start_the_game(self) -> ClassVar:
        if self.__game == 1:
            return game_number_guessing.NumberGuessingGame()
        elif self.__game == 2:
            return game_hangman.HangmanGame()
        elif self.__game == 3:
            return game_twenty_one.TwentyOneGame()


if __name__ == '__main__':
    while True:
        print()
        PythonGames()
        print()
        if call_the_game_list() != 'Y':
            break
