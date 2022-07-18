from random import randint

from constants import (limit_below, limit_above, start_score_N,
                       num_attempts_l1, num_attempts_l2, num_attempts_l3,
                       input_of_the_variable)


class NumberGuessingGame:
    def __init__(self) -> None:
        self.__level: int = self.__input_of_the_level()
        self.__number_of_attempts = self.__select_the_number_of_attempts()
        self.__number_chosen = randint(limit_below, limit_above)
        self.__score = start_score_N
        self.__play()

    @staticmethod
    def __header() -> None:
        print('NUMBER GUESSING GAME')
        print(f'Try to guess the number chosen between {limit_below} and'
              f' {limit_above}.')
        print(f'The game starts with {start_score_N} points. For each wrong'
              f' kick, a number of points is deducted.')
        print(f'The amount of points deducted depends on the difference'
              f' between the number entered and the number chosen.\n')
        print('GAME LEVELS')
        print(f'[1] Level 1 ({num_attempts_l1:02} attempts)\n'
              f'[2] Level 2 ({num_attempts_l2:02} attempts)\n'
              f'[3] Level 3 ({num_attempts_l3:02} attempts)')

    def __input_of_the_level(self) -> int:
        self.__header()
        return input_of_the_variable('Choose a level: ',
                                     'Error! Choose one of the 3 levels.',
                                     3, 1
                                     )

    def __select_the_number_of_attempts(self) -> int:
        if self.__level == 1:
            return num_attempts_l1
        elif self.__level == 2:
            return num_attempts_l2
        elif self.__level == 3:
            return num_attempts_l3

    @staticmethod
    def __input_of_the_guess(count) -> int:
        return input_of_the_variable(f'Guess {count + 1}. Choose a number'
                                     f' between {limit_below} and'
                                     f' {limit_above}: ',
                                     f'Error! Choose a number between'
                                     f' {limit_below} and {limit_above}.',
                                     limit_above, limit_below
                                     )

    def __evaluate_the_guess(self, guess, count) -> int:
        if guess > self.__number_chosen:
            if count < self.__number_of_attempts - 1:
                print(f'Try again. The number is less than the {guess}.')
            return guess - self.__number_chosen
        elif guess < self.__number_chosen:
            if count < self.__number_of_attempts - 1:
                print(f'Try again. The number is bigger than {guess}.')
            return self.__number_chosen - guess
        else:
            return 0

    def __play(self) -> None:
        count: int = 0
        while count < self.__number_of_attempts:
            guess: int = self.__input_of_the_guess(count)
            result: int = self.__evaluate_the_guess(guess, count)
            self.__score -= result
            if result == 0 or self.__score < 1:
                if result == 0:
                    print(f'Congratulations! The number is'
                          f' {self.__number_chosen} and your score is'
                          f' {self.__score}.')
                else:
                    print(f'Try again. You are out of score.')
                    print(f'The number is {self.__number_chosen} and your'
                          f' score is {self.__score}.')
                break
            else:
                count += 1
                if count == self.__number_of_attempts:
                    print(f'Try again. You passed the number of attempts. ')
                    print(f'The number is {self.__number_chosen} and your'
                          f'score is {self.__score}.')
                    break


if __name__ == '__main__':
    NumberGuessingGame()
