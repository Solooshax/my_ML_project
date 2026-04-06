import face_recognition
import numpy as np
from database.mongo_db import users_collection

def verify_face(image):

    rgb = image

    faces = face_recognition.face_locations(rgb)

    if len(faces) == 0:
        return False

    encoding = face_recognition.face_encodings(rgb, known_face_locations=faces)[0]

    users = users_collection.find()

    for user in users:

        if "face_encoding" not in user:
            continue

    saved_encoding = np.array(user["face_encoding"])

    match = face_recognition.compare_faces(
        [saved_encoding],
        encoding
    )[0]

    if match:
        return user["email"]

    return None