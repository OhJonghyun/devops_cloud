import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 03. 좋아요 수가 200000이 넘는 곡 수는?

count = 0
for song in song_list:
    if song["like"] > 200000:
        count += 1
print(count) # print(f"좋아요가 200,000이 넘는 곡은 {song_count}곡입니다.""))
