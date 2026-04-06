from flask import Blueprint, request, jsonify
import os

from emotion_detection.emotion_predict import predict_emotion

emotion_bp = Blueprint("emotion", __name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@emotion_bp.route("/detect-emotion", methods=["POST"])
def detect_emotion():

    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]

    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    emotion = predict_emotion(file_path)

    return jsonify({
        "emotion": emotion
    })
