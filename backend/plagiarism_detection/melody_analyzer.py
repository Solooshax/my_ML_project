import librosa
import numpy as np
import os
import pickle


DATABASE_FOLDER = "song_database"
FEATURE_FILE = "plagiarism_detection/feature_database.pkl"


def extract_features(file_path):

    try:

        y, sr = librosa.load(file_path, duration=30)

        window_size = sr * 5

        mfcc = librosa.feature.mfcc(y=y[:window_size], sr=sr)
        chroma = librosa.feature.chroma_stft(y=y[:window_size], sr=sr)
        contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        features = np.hstack([
            np.mean(mfcc, axis=1),
            np.mean(chroma, axis=1),
            np.mean(contrast, axis=1),
            tempo
        ])

        features = features / np.linalg.norm(features)

        return features

    except Exception as e:

        print("Feature extraction failed for:", file_path)
        print("Reason:", e)

        return None
    

def build_feature_database():

    feature_db = {}

    for genre in os.listdir(DATABASE_FOLDER):

        genre_path = os.path.join(DATABASE_FOLDER, genre)

        if not os.path.isdir(genre_path):
            continue

        for song in os.listdir(genre_path):

            song_path = os.path.join(genre_path, song)

            print("Processing:", song_path)

            try:
               features = extract_features(song_path)
               feature_db[song_path] = features

            except Exception as e:
               print("Skipped file:", song_path)
               print("Reason:", e)

    with open(FEATURE_FILE, "wb") as f:
        pickle.dump(feature_db, f)

    print("Feature database created.")


def load_feature_database():

    with open(FEATURE_FILE, "rb") as f:
        database = pickle.load(f)

    return database


def compare_song(upload_path):

    database = load_feature_database()

    query_features = extract_features(upload_path)

    best_match = None
    best_score = 0

    for song, features in database.items():

        similarity = np.dot(query_features, features) / (
            np.linalg.norm(query_features) * np.linalg.norm(features)
)

    if similarity > best_score:
            best_score = similarity
            best_match = song

    return best_match, best_score

def compare_songs(query_file, database_file):

    query_features = extract_features(query_file)
    db_features = extract_features(database_file)

    if query_features is None or db_features is None:
        return 0

    similarity = sliding_similarity(query_file, database_file)
        
    return similarity


def sliding_similarity(query_file, database_file):

    try:

        query_features = extract_features(query_file)
        db_features = extract_features(database_file)

        if query_features is None or db_features is None:
            return 0

        similarity = np.dot(query_features, db_features)

        return similarity

    except Exception as e:

        print("Sliding similarity failed:", database_file)
        print("Reason:", e)

        return 0