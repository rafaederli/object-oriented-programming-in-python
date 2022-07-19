import re
from collections import Counter
from typing import Dict, TextIO, Pattern, Optional, Match


class CountLetters:
    def __init__(self, text_file: str) -> None:
        self.__raw_text: str = self.__read_the_text_file(text_file)
        self.__just_letters: str = self.__treat_the_raw_text()

    @staticmethod
    def __read_the_text_file(text_file: str):
        file: TextIO = open(text_file, 'r')
        raw_text: str = file.read()
        file.close()
        return raw_text

    @staticmethod
    def __is_in_the_alphabet(letter: str):
        pattern: Pattern[str] = re.compile('[aA-zZ]')
        match: Optional[Match[str]] = re.match(pattern, letter)
        if match:
            return True

    def __treat_the_raw_text(self) -> str:
        return ''.join([letter for letter in self.__raw_text
                        if letter.isalpha()
                        and self.__is_in_the_alphabet(letter)]).upper()

    @property
    def absolute_frequency(self) -> Counter:
        """
        This method returns a collection sorted by the absolute frequency
        of each letter
        :return: Counter class object
        """
        return Counter(self.__just_letters)

    @property
    def relative_frequency(self) -> Dict:
        """
        This method returns a dictionary ordered by the relative frequency
        of each letter
        :return: Dict class object
        """
        return dict(sorted([(letter, round(
            frequency / len(self.__just_letters), 4)
                             ) for letter, frequency in
                            self.absolute_frequency.items()],
                           reverse=True, key=lambda element: element[1]))
