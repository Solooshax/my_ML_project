from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = "mongodb+srv://shaziya_db_user:ttXfsgVtpxLWz2YK@ai-music-db.ngkit2i.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["ai_music_database"]

users_collection = db["users"]

print("MongoDB Connected Successfully")