from flask import Blueprint, request, jsonify
import os

from lyrics_analysis.speech_to_text import convert_speech_to_text
from voice_emotion.voice_predict import predict_emotion

from sentiment import get_sentiment

# updated import for smart recommendation
from music_recommendation.recommender import recommend_songs

# these imports are for plagiarim_detection
from plagiarism_detection.melody_analyzer import compare_songs

audio_bp = Blueprint("audio_analysis", __name__)

UPLOAD_FOLDER = "uploads"


@audio_bp.route("/analyze-audio", methods=["POST"])
def analyze_audio():

    if "audio" not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files["audio"]

    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    import subprocess

    wav_path = file_path.rsplit(".", 1)[0] + ".wav"

    subprocess.call([
        "ffmpeg",
        "-y",         
        "-i", file_path,
        wav_path
    ])

    file_path = wav_path

    transcript = convert_speech_to_text(file_path)

    emotion = predict_emotion(file_path).lower()

    # NLP sentiment
    text_emotion = get_sentiment(transcript)

    print("Audio emotion:", emotion)
    print("Text emotion:", text_emotion)

    # HYBRID LOGIC
    if emotion in ["neutral", "calm"]:
        final_emotion = text_emotion
    else:
        final_emotion = emotion

    # SMART RECOMMENDATION (NEW)
    playlist = recommend_songs(final_emotion)

    return jsonify({
        "transcript": transcript,
        "emotion": final_emotion,
        "playlist": playlist
    })


@audio_bp.route("/check-plagiarism", methods=["POST"])
def check_plagiarism():

    audio_file = request.files["audio"]

    file_path = os.path.join("uploads", audio_file.filename)
    audio_file.save(file_path)

    database_folder = "song_database"

    best_match = None
    best_score = 0

    for genre in os.listdir(database_folder):

        genre_path = os.path.join(database_folder, genre)

        if not os.path.isdir(genre_path):
            continue

        for song in os.listdir(genre_path):

            if not song.endswith(".wav"):
                continue

            song_path = os.path.join(genre_path, song)

            score = compare_songs(file_path, song_path)

            if score > best_score:
                best_score = score
                best_match = f"{genre}/{song}"

    return jsonify({
        "match_song": best_match,
        "similarity": float(round(best_score * 100, 2))
    })