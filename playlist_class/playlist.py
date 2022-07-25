from typing import List


class Playlist:
    def __init__(self, media_list) -> None:
        self.__media_list = media_list

    def __getitem__(self, item) -> List:
        return self.__media_list[item]
