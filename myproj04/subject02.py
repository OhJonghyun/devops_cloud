import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 02.곡명에 "가을"이 들어가는 곡명만 출력해보세요.
# 가을 in 제목

for song in song_list:
    if "가을" in song["title"]: #문자열, 튜블, 사전 전부 다 들어올 수 있음.
        print(song["title"])
