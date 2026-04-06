from database.mongo_db import users_collection

data = {
    "email": "test@gmail.com",
    "password": "123456"
}

users_collection.insert_one(data)

print("User inserted successfully")