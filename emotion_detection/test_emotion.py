from emotion_predict import predict_emotion

file = "emotion_detection/dataset/Actor_01/03-01-01-01-01-01-01.wav"

emotion = predict_emotion(file)

print("Predicted Emotion:", emotion)