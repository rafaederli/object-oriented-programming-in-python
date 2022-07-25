class Media:
    def __init__(self, title: str, year: int, genre: str) -> None:
        self._title: str = title.title()
        self._year: int = year
        self._genre: str = genre

    @property
    def title(self) -> str:
        return self._title

    @property
    def year(self) -> int:
        return self._year

    @property
    def genre(self) -> str:
        return self._genre


class Movie(Media):
    def __init__(self, title: str, year: int, genre: str,
                 duration: int) -> None:
        super().__init__(title, year, genre)
        self.__duration: int = duration

    @property
    def duration(self) -> int:
        return self.__duration

    def __str__(self) -> str:
        return (f'Title: {self._title:40} '
                f'Year: {self._year:4} '
                f'Genre: {self._genre:10} '
                f'Duration: {self.__duration:3} minutes')


class Series(Media):
    def __init__(self, title: str, year: int, genre: str,
                 duration: int):
        super().__init__(title, year, genre)
        self.__duration: int = duration

    @property
    def duration(self) -> int:
        return self.__duration

    def __str__(self) -> str:
        return (f'Title: {self._title:40} '
                f'Year: {self._year:4} '
                f'Genre: {self._genre:10} '
                f'Duration: {self.__duration:3} seasons')
