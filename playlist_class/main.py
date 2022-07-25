from typing import List, Union

from media_classes import Movie, Series
from playlist import Playlist


# Error handling
def get_an_integer(input_text: str) -> int:
    while True:
        try:
            integer: int = int(input(input_text))
        except ValueError:
            print('Error! Type an integer.')
            print()
        else:
            break
    return integer


def get_a_letter(input_text: str, key1: str, key2: str) -> str:
    while True:
        letter: str = input(input_text).strip().upper()[0]
        if letter not in (key1[0], key2[0]):
            print(f'Error! Type {key1} or {key2}')
            print()
        else:
            break
    return letter


media_list: List[Union[Movie, Series]] = []
while True:
    media: str = get_a_letter(input_text='Media type [Movie or Series]: ',
                              key1='Movie', key2='Series')
    title: str = input('Title: ').strip().upper()
    year: int = get_an_integer('Release year: ')
    genre: str = input('Genre: ')

    if media == 'M':
        duration_movie: int = get_an_integer('Duration (minutes): ')
        movie: Movie = Movie(title, year, genre, duration_movie)
        media_list.append(movie)
    else:
        duration_series: int = get_an_integer('Duration (seasons): ')
        series: Series = Series(title, year, genre, duration_series)
        media_list.append(series)

    playlist: Playlist = Playlist(media_list)

    print()
    for media in playlist:
        print(media)
    print()
