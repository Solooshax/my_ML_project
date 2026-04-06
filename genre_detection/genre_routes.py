from flask import Blueprint, request, jsonify
import os

from genre_detection.genre_predict import predict_genre

genre_bp = Blueprint("genre_detection", __name__)

UPLOAD_FOLDER = "uploads"


@genre_bp.route("/detect-genre", methods=["POST"])
def detect_genre():

    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files["audio"]

    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)

    audio_file.save(file_path)

    genre = predict_genre(file_path)

    return jsonify({
        "genre": genre
    })