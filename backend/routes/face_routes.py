from database.mongo_db import users_collection
from flask import Blueprint, request, jsonify, render_template
from face_login.face_register import register_face
from face_login.face_login import verify_face
import numpy as np
import base64
import cv2


face_bp = Blueprint("face_bp", __name__)

# Register page
@face_bp.route("/register")
def register_page():
    return render_template("face_register.html")

# Login page
@face_bp.route("/login")
def login_page():
    return render_template("face_login.html")


def decode_image(base64_image):

    # remove base64 header
    header, encoded = base64_image.split(",", 1)

    img_data = base64.b64decode(encoded)

    np_arr = np.frombuffer(img_data, np.uint8)

    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Image decoding failed")

    # ensure correct dtype
    img = img.astype(np.uint8)

    # convert BGR → RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


@face_bp.route("/register-face", methods=["POST"])
def register_face_api():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    image_data = data.get("image")

    if not email or not image_data:
        return jsonify({"success": False, "message": "Missing data"}), 400

    image = decode_image(image_data)

    success, message = register_face(image, email, password)

    return jsonify({
        "success": success,
        "message": message
    })

@face_bp.route("/login-face", methods=["POST"])
def login_face_api():

    data = request.get_json()

    image_data = data.get("image")

    if not image_data:
        return jsonify({"success": False, "message": "No image"}), 400

    image = decode_image(image_data)

    user_email = verify_face(image)

    if user_email:
        return jsonify({
            "success": True,
            "message": "Login successful"
        })

    else:
        return jsonify({
            "success": False,
            "message": "Face not recognised"
        })
    
@face_bp.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")