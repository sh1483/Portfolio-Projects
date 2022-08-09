# Use 8_7.py and write a while loop that allows user input for album title and,
# Artist. Ensure you use a quit value in the while loop.
def make_album(artist, album, tracks=None):
    """Build a dictionary of information about an album"""
    album_dict = {
        'name': artist.title(),
        'album': album.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Make the prompts.
artist_prompt = "\nArtist name: "
title_prompt = "Album name: "

# Let them know how to quit.
print("(enter 'q' a any time to quit)")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = input(title_prompt)
    if album == 'q':
        break

    album = make_album(artist, album)
    print(album)

print("\nThanks for responding!")
