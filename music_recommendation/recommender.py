import random
from music_recommendation.music_data import music_library

last_history = []

def recommend_songs(emotion, k=5):
    global last_history

    # ✅ smart fallback (neutral best hai)
    songs = music_library.get(emotion, music_library["neutral"])

    # avoid repeat
    new_songs = [s for s in songs if s not in last_history]

    if len(new_songs) < k:
        new_songs = songs

    random.shuffle(new_songs)

    selected = new_songs[:k]

    # update history (last 10 songs)
    last_history = (last_history + selected)[-10:]

    return selected