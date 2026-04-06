import face_recognition
import numpy as np
from database.mongo_db import users_collection


def register_face(image, email, password):

    faces = face_recognition.face_locations(image)

    if len(faces) == 0:
        return False, "No face detected"

    encodings = face_recognition.face_encodings(image, faces)

    if len(encodings) == 0:
        return False, "Face encoding failed"

    encoding = encodings[0]

    # convert numpy array to list (MongoDB compatible)
    encoding_list = encoding.tolist()

    # check if user already exists
    existing_user = users_collection.find_one({"email": email})

    if existing_user:
        return False, "User already registered"

    # save user in MongoDB
    users_collection.insert_one({
        "email": email,
        "password": password,
        "face_encoding": encoding_list
    })

    return True, "Face registered successfully"