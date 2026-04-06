import librosa
import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "genre_model.pkl")

model = joblib.load(model_path)


def extract_features(file_path):

    audio, sr = librosa.load(file_path, duration=30)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

    mfcc = np.mean(mfcc.T, axis=0)

    return mfcc


def predict_genre(file_path):

    features = extract_features(file_path)

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    return prediction[0]