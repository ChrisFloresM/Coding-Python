#Christian Flores 12/02/2021

def make_album(artist_name, album_title, number_of_songs = None):
    album = {}
    album["artist"] = artist_name
    album["title"] = album_title
    if number_of_songs:
        album["Amount of songs"] = number_of_songs
    return album

album_1 = make_album(artist_name = "The Killers", album_title = "Wonderful Wonderful")
album_2 = make_album("Stevie Nicks", "The other side of the mirror")
album_3 = make_album(album_title = "Bad Animals", artist_name = "Heart")
album_4 = make_album("The Killers", "Battle Born", number_of_songs = 10)

print(album_1)
print(album_2)
print(album_3)
print(album_4)