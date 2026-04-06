from flask_cors import CORS
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template
from routes.emotion_routes import emotion_bp
from routes.audio_analysis_routes import audio_bp
from routes.face_routes import face_bp
from routes.region_routes import region_bp
from genre_detection.genre_routes import genre_bp

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


# emotion detection
app.register_blueprint(emotion_bp)

# lyrics analysis
app.register_blueprint(audio_bp)

# face login 
app.register_blueprint(face_bp, url_prefix="")

# region detection
app.register_blueprint(region_bp)

# genre detection
app.register_blueprint(genre_bp)

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
