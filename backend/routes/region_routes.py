from flask import Blueprint, request, jsonify
import os

from regional_detection.region_predict import predict_region

region_bp = Blueprint("region_detection", __name__)

UPLOAD_FOLDER = "uploads"

@region_bp.route("/detect-region", methods=["POST"])
def detect_region_api():

    if "audio" not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files["audio"]

    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    # ML MODEL PREDICTION

    region = predict_region(file_path)

    # REGION (country)
    region_map = {
        "english": "USA / UK",
        "bollywood": "India",
        "arabic": "Middle East",
        "french": "France",
        "spanish": "Spain",
        "korean": "Korea"
    }

    # LANGUAGE (actual language)
    language_map = {
        "english": "English",
        "bollywood": "Hindi / Urdu / Punjabi",
        "arabic": "Arabic",
        "french": "French",
        "spanish": "Spanish",
        "korean": "Korean"
    }

    final_region = region_map.get(region.lower(), "Unknown")
    final_language = language_map.get(region.lower(), "Unknown")

    return jsonify({
        "language": final_language,
        "region": final_region
})