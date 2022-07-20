import re
from typing import Pattern, Optional, Match, Dict


class ExtractURL:
    def __init__(self, url: str) -> None:
        self.__url: str = self.__validate_url(url)
        self.__url_delimiter: int = self.__url.find('?')
        self.__url_parameters: str = self.__url[self.__url_delimiter + 1:]
        self.__number_parameters: int = self.__url_parameters.count('&') + 1

    @staticmethod
    def __validate_url(raw_url) -> str:
        """
        This method evaluates if the URL matches the default URL and if
        contains parameter and value
        :param url: URL
        :return: URL
        """
        url: str = raw_url.replace(' ', '')
        pattern: Pattern = \
            re.compile('(http(s)?://)?(www.)?[a-z.]+.com(.br)?/(a-z)?')
        match: Optional[Match[str]] = pattern.match(url)
        if not match:
            raise ValueError('The URL is not valid.')
        elif '=' not in url:
            raise ValueError('The URL does not contain parameter and value.')
        else:
            return url

    @property
    def extract_parameters_and_values(self) -> Dict[str, str]:
        """
        This method extracts the parameters and their values from the URL
        :return: Dictionary-type object with parameters and values
        """
        parameters_and_values: Dict[str, str] = {}
        for element in range(self.__number_parameters):
            if element == 0:
                parameters_delimiter_le: int = - 1
                parameters_delimiter_ri: int = self.__url_parameters.find('&')
                parameter_value_delimit: int = self.__url_parameters.find('=')
            else:
                parameters_delimiter_le: int =\
                    self.__url_parameters.find('&',
                                               parameters_delimiter_le + 1)
                parameters_delimiter_ri: int =\
                    self.__url_parameters.find('&',
                                               parameters_delimiter_ri + 1)
                parameter_value_delimit: int =\
                    self.__url_parameters.find('=',
                                               parameter_value_delimit + 1)

            parameter: str = \
                self.__url_parameters[parameters_delimiter_le + 1:
                                      parameter_value_delimit]
            value: str = \
                self.__url_parameters[parameter_value_delimit + 1:
                                      parameters_delimiter_ri
                                      if element <
                                      self.__number_parameters - 1 else None]
            parameters_and_values[parameter] = value
        return parameters_and_values
