from typing import List, TextIO

# Number Guessing Game
limit_below: int = 1
limit_above: int = 100
start_score_N: int = 1000
num_attempts_l1: int = 20
num_attempts_l2: int = 10
num_attempts_l3: int = 5

# Hangman Game
num_attempts: int = 10

# Twenty One Number Game
start_score_T: int = 100


# Methods
def input_of_the_variable(input_message: str,
                          error_message: str,
                          lim_above: int,
                          lim_below: int = 0) -> int:
    while True:
        try:
            number: int = int(input(input_message))
        except ValueError:
            print()
            print(error_message)
        else:
            if number > lim_above or number < lim_below:
                print()
                print(error_message)
            else:
                print()
                break
    return number


def call_the_game_list() -> str:
    while True:
        try:
            action: str = input('Would you like '
                                'to play more? [Y/N] ').strip().upper()[0]
        except IndexError:
            print('Error! Type Yes or No.')
        else:
            if action not in 'YN' or action == '':
                print('Error! Type Yes or No.')
            else:
                break
    return action


def read_a_text_file(text_file: str) -> List[str]:
    try:
        file: TextIO = open(text_file, 'r')
    except FileNotFoundError:
        print('Error! File not found in the directory.')
    else:
        lst: List[str] = [element.strip() for element in file]
        file.close()
        return lst


def convert_list_to_string(lst: List[str], sep: str = '') -> str:
    return sep.join(lst)
