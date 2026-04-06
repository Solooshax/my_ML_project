import numpy as np 
import librosa 
import joblib 
import os 
from tensorflow.keras.models import load_model 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

model_path = os.path.join(BASE_DIR, "models", "emotion_model.h5") 
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = load_model(model_path) 
scaler = joblib.load(scaler_path) 
label_encoder = joblib.load(os.path.join(BASE_DIR, "models", "label_encoder.pkl"))

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, duration=3, offset=0.5)

    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)

    return mfcc

def predict_emotion(file_path):

    features = extract_features(file_path)

    features = np.array(features).reshape(1, -1) 
    features = scaler.transform(features) 

    prediction = model.predict(features)

    print("Prediction probabilities:", prediction) 
    print("Predicted index:", np.argmax(prediction)) 

    predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])[0]
    print("Emotion predicted:", predicted_label)

    emotion = predicted_label
    
    return emotion
