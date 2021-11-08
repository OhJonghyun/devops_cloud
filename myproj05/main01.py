import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict)
        # print(song_dict["title"], song_dict["artist"], song_dict["like"])
        # print 에 sep 인자는 default 값이다.

        # line(song_dict["title"], song_dict["artist"], song_dict["like"])
        # line = "{}, {}, {}".format(
        #    song_dict["title"], song_dict["artist"], song_dict["like"]
        # )
        # print(line)

        # line = "{가수명}, {곡명}, {좋아요수}".format(
        #    곡명=song_dict["title"], 가수명=song_dict["artist"], 좋아요수=song_dict["like"]
        # )
        # print(line)

        # line = "{title}, {artist}, {like}".format(
        #    title=song_dict["title"], artist=song_dict["artist"], like=song_dict["like"]
        # )
        # print(line)

        # unpack argument : 순수하게 사전에 있는 부분만 가능
        # line = "{title}, {artist}, {like}".format(**song_dict)
        # print(line)

# list comprehension
# fmt : off
artist_list = [song_dict["artist"] for song_dict in song_list]

# #fmt : on
# counter = Counter(artist_list)
# #for artist in counter: # keys
# #    print(artist)

# for artist in counter.values():     # values
#     print(artist)

for artist, song_count in counter.items():
    print(artist, song_count)
