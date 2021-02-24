#Christian Flores 12/02/2021

#Christian Flores 12/02/2021

def make_album(artist_name, album_title, number_of_songs = None):
    album = {}
    album["artist"] = artist_name
    album["title"] = album_title
    if number_of_songs:
        album["Amount of songs"] = number_of_songs
    return album

new_album = True
while new_album:
    print("\nEnter 'q' anytime to stop searching for albums")
    album_name = input("Album name: ")
    if album_name == "q":
        break
    artist = input("Artist: ")
    if artist == "q":
        break
    songs = input("Number of songs: ")
    if songs == "q":
        break
    album_dict = make_album(artist, album_name, songs)
    print(f"\nDictionary: {album_dict}")

