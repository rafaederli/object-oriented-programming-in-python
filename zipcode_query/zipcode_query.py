import requests
from typing import Dict


class ZipCodeQuery:
    def __init__(self, zipcode: str) -> None:
        self.__data: Dict[str, str] = self.__validate_zipcode(zipcode)

    @staticmethod
    def __get_json_file(zipcode: str) -> Dict[str, str]:
        r: requests.models.Response = \
            requests.get(f'https://viacep.com.br/ws/{zipcode}/json/')
        file: Dict[str, str] = r.json()
        return file

    def __validate_zipcode(self, zipcode: str) -> Dict[str, str]:
        zipcode: str = ''.join([element for element in zipcode
                                if element.isnumeric()])
        if len(zipcode) == 8:
            file: Dict[str, str] = self.__get_json_file(zipcode)
            if 'erro' in file:
                raise ValueError('Zip Code not found.')
            else:
                return file
        else:
            raise ValueError('The Zip Code does not have 8 numbers.')

    def __zipcode_formatted(self) -> str:
        zipcode: str = self.__data["cep"]
        return f'{zipcode[0:2]}.{zipcode[2:]}'

    def __str__(self) -> str:
        return f'Zip Code: {self.__zipcode_formatted()}\n' \
               f'Address: {self.__data["logradouro"]}\n' \
               f'District: {self.__data["bairro"]}\n' \
               f'City: {self.__data["localidade"]}\n' \
               f'State: {self.__data["uf"]}'
