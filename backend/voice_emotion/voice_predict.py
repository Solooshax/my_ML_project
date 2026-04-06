import numpy as np
import librosa
import joblib
from tensorflow.keras.models import load_model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = load_model(os.path.join(BASE_DIR, "models", "voice_emotion_model.h5"))
encoder = joblib.load(os.path.join(BASE_DIR, "models", "voice_label_encoder.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "voice_scaler.pkl"))

print("Classes:", encoder.classes_)

def extract_features(file_path):

    audio, sr = librosa.load(file_path, sr=22050)

    # remove silence
    audio, _ = librosa.effects.trim(audio, top_db=20)

    # normalize volume
    audio = librosa.util.normalize(audio)

    if np.max(audio) == 0:
        return np.zeros(40)

    if len(audio) < 3 * sr:
        audio = np.pad(audio, (0, 3 * sr - len(audio)))
    else:
        audio = audio[:3 * sr]

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)

    return mfcc

def predict_emotion(file_path):

    features = extract_features(file_path)
    features = scaler.transform([features])

    prediction = model.predict(features)

    # temperature scaling
    temperature = 1.2
    exp_preds = np.exp(prediction / temperature)
    prediction = exp_preds / np.sum(exp_preds, axis=1, keepdims=True)

    print("Prediction probs:", prediction)

    top1 = np.argmax(prediction[0])
    max_prob = prediction[0][top1]

    print("Top1:", top1, "Confidence:", max_prob)
    
    # low confidence → neutral
    if max_prob < 0.35:
        return "neutral"

    emotion = encoder.inverse_transform([top1])[0]

    print("Final emotion:", emotion)

    return emotion