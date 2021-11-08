import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# print(song_list)


# 방탄소년단의 곡명만 출력해보세요.

for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])
