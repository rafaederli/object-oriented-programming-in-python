from random import choice
from typing import List

from constants import num_attempts, read_a_text_file, convert_list_to_string


class HangmanGame:
    def __init__(self) -> None:
        self.__secret_word: str = choice(self.__read_the_word_list()).upper()
        self.__number_of_attempts: int = num_attempts
        self.__play()

    @staticmethod
    def __header() -> None:
        print('HANGMAN GAME')
        print(f'Try to guess the secret word.')
        print(f'Tip: It is a fruit name.\n')

    @staticmethod
    def __read_the_word_list() -> List[str]:
        return read_a_text_file('fruit_name_list.txt')

    @staticmethod
    def __input_of_a_letter() -> str:
        while True:
            try:
                letter: str = input('Choose a letter: ').strip().upper()[0]
            except IndexError:
                print('Error! Choose a letter.')
            else:
                if letter.isnumeric():
                    print('Error! Choose a letter.')
                else:
                    break
        return letter

    def __play(self) -> None:
        count: int = 0
        formed_word_list: List[str] = ['_'] * len(self.__secret_word)
        guesses_list: List[str] = []
        self.__header()
        while count < self.__number_of_attempts:
            formed_word: str = convert_list_to_string(formed_word_list, sep=' ')
            guesses: str = convert_list_to_string(guesses_list, sep=', ')

            if formed_word.replace(' ', '') == self.__secret_word:
                print(f'\nCongratulations. You got the word right.')
                print(f'The word is {self.__secret_word}.')
                break

            print(f'Word: {formed_word}\nGuesses: {guesses}')

            print(f'\nGuess {count + 1}', end='. ')
            letter: str = self.__input_of_a_letter()

            if letter in self.__secret_word:
                for index, char in enumerate(self.__secret_word):
                    if letter == char:
                        formed_word_list[index]: List[str] = letter
            else:
                guesses_list.append(letter)
                count += 1
                if count == self.__number_of_attempts:
                    print('\nTry again. You passed the number of attempts.')
                    print(f'The word is {self.__secret_word}')
                    break


if __name__ == '__main__':
    HangmanGame()
