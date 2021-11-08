from collections import Counter
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 04. 가수 별 곡수를 출력해보세요.

# singer = []
# for song in song_list:
#    singer.append(song["artist"])
#
# singer_1 = {}
# for ch in singer:
#    try:
#        singer_1[ch] += 1
#    except KeyError:
#       singer_1[ch] = 1
# print(singer_1)

# artist_dict = {}

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist not in artist_dict:
#         artist_dict[artist] = 0
#     artist_dict[artist] += 1

# print(artist_dict)

# artist_list - []
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     artist_list.append(artist)

# print(counter(artist_list))

artist_list = [song_dict["artist"] for song_dict in song_list]

print(Counter(artist_list))
