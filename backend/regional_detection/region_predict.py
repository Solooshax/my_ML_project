import librosa
import numpy as np
import joblib

model = joblib.load("regional_detection/region_model.pkl")

def extract_features(file_path):
    audio, sr = librosa.load(file_path, duration=30)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

def predict_region(file_path):
    features = extract_features(file_path)
    features = features.reshape(1, -1)

    prediction = model.predict(features)

    return prediction[0]