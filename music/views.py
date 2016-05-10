from django.shortcuts import render
from musicplayer.settings import SONGS_PATH
import os


def index(request):
    context = {
        "songs": get_songs(),
    }
    print(context)
    return render(request, "index.html", context)


# Return a list of file paths each to a song file
def get_songs():
    song_names = os.listdir(SONGS_PATH)
    songs = []
    for song_name in song_names:
        filepath = os.path.join('songs/', song_name)
        song_name_clean = song_name.replace(".mp3", "").replace("_", " ")

        song = {
            "name": song_name_clean,
            "url": filepath
        }
        songs.append(song)
    return songs
