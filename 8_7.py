# Write a function to build a dictionary describing music albums. It should take in,
# Artist, Album Name, and an optional space for Number of Tracks.
def make_album(artist_name, album_name, tracks=None):
    """Return a dictionary of information about an album"""
    album = {'name': artist_name, 'album': album_name}
    if tracks:
        album['tracks'] = tracks
    return album


musician = make_album('metallica', 'and justice for all')
print(musician)

musician = make_album('pantera', 'cowboys from hell')
print(musician)

musician = make_album('dido', 'life for rent', tracks=12)
print(musician)
