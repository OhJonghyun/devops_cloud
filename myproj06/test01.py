from pprint import pprint
from typing import List  # Type Hinting
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def check_bts_song(song_dict):
    """
    BTS 노래라면 True를 반환합니다.
    """
    # 함수 시작하자마자 문자열로 써야함.
    # BTS 노래라면 Ture를 리턴
    # 아니라면 False를 리턴
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


new_song_list: List[dict] = []

for song_dict in song_list:
    if check_bts_song(song_dict):
        # artist: str = song_dict["artist"]
        # if artist == "방탄소년단":
        new_song_list.append(song_dict)

    # title_list.append(song_dict["title"])
    # song_dict["title"]

pprint(new_song_list)


def check_above_200_000(song_dict):
    like: int = song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200_000, song_list):
    print("{title} - {like}".format(**song_dict))
