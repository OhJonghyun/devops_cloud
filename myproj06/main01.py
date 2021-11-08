"""
"방탄소년단" 곡명만 출력하기
곡명에 "사랑"이 포함된 곡명만 출력하기
"좋아요" 수가 2000 이상 300000이하 곡명만 출력하기
"""

from pprint import pprint
from typing import List  # Type Hinting
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
"방탄소년단" 곡명만 문자열로 구성된 리스트를 만들어보세요.
"""

# title_list: List[str] = []  # title list인데 문자열로만 표현한다.
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         title: str = song_dict["title"]
#         title_list.append(title)
#     # title_list.append(song_dict["title"])
#     # song_dict["title"]

# print(title_list)

# new_song_list: List[dict] = []  # title list인데 문자열로만 표현한다.

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         new_song_list.append(song_dict)
#     # title_list.append(song_dict["title"])
#     # song_dict["title"]

# pprint(new_song_list)


def check_bts_song(song_dict):
    """
    BTS 노래라면 True를 반환합니다.
    """
    # 함수 시작하자마자 문자열로 써야함.
    # BTS 노래라면 Ture를 리턴
    # 아니라면 False를 리턴
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


# new_song_list: list[dict] = []
new_song_list: list(filter(check_bts_song, song_list))
print(new_song_list)
# 단순히 print만 한다라고 하면
for song_dict in filter(check_bts_song, song_list):
    print("{title} {artist} {like}".format(**song_dict))
for song_dict in song_list:
    if check_bts_song(song_dict):
        # artist: str = song_dict["artist"]
        # if artist == "방탄소년단":
        new_song_list.append(song_dict)

    # title_list.append(song_dict["title"])
    # song_dict["title"]

pprint(new_song_list)

"""
곡명에 "사랑"이 포함된 곡들의 곡명 리스트를 만들어보세요.
"""


def check_contains_love(song_dict):
    title: str = song_dict["title"]
    return "사랑" in title


for song_dict in filter(check_contains_love, song_list):
    print("{title}}".foramt(**song_dict))


# title_list: list[str] = []

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     if "사랑" in title:  # in은 목록의 성격을 가진 값들이 뒤에 온다. (tuple, list)
#         title_list.append(title)

# print(title_list)

""""
좋아요" 수가 2000 이상 300000이하 곡들의 곡명 리스트를 만들어보세요.
"""


def check_above_200_000(song_dict):
    like: int = song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200_000, song_list):
    print("{title} - {like}".format(**song_dict))
# title_list: list[str] = []
# for song_dict in song_list:
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     if like >= 200_000:
#         title_list.append(title)

# print(title_list)
