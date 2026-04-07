# 🎵 AI Music Intelligence System

An intelligent AI-based system that analyzes music using multiple features like emotion detection, genre classification, regional detection, plagiarism detection, and recommendation.


# 🚀 Features

* 🔐 Face Recognition Login & Registration   (secure login)
* 😊 Emotion Detection                       (via audio upload)
* 🎤 Voice Emotion Detection                 (live via microphone recording)
* 🧠 Text Emotion Detection (NLP)            (sentiment analysis)
* 🎼 Genre Detection                         (Detects genre of music)
* 🌍 Regional Detection                      (Detects region of the song)
* 🔍 Plagiarism Detection                    (Detects plagiarism of the song)
* 🎧 Music Recommendation System             (Recommends music based on emotion)



# 📥 Download Required Data

Download this folder: 👉 **AI_Music_Data**
(Google Drive link) : https://drive.google.com/drive/folders/1py-dO5N0zHSck1JQBOrwlveQyjyjYQTR?usp=sharing



# After downloading the zip file (📂 AI_Music_Data )  you will see Folder Structure something like this:

AI_Music_Data/
  🔹backend_uploads/
  🔹emotion_detection_dataset/
  🔹voice_emotion_detection_dataset/
  🔹regional_detection_dataset/
  🔹plagiarism_detection_database/
  🔹models/



# ⚙️ SETUP (VERY IMPORTANT)

**Step 1: Clone the Repository**
Open terminal / command prompt and run:

git clone https://github.com/Solooshax/my_ML_project
   
cd my_ML_project


**Step 2: Install Required Libraries**
Make sure Python is installed, then run:

pip install -r requirements.txt



## 🔹 1. Place MODELS into PROJECT (REQUIRED ✅)

 **🧠 Emotion Detection**

 **From:**
AI_Music_Data/models/emotion_detection/

**➡ Copy all files to:**
emotion_detection/models/

**🎤 Voice Emotion Detection**

**From:**
AI_Music_Data/models/voice_emotion_detection/

**➡ Copy all files to:**
backend/voice_emotion/models/

**🎼 Genre Detection**

**From:**
AI_Music_Data/models/genre_detection/genre_model.pkl

**➡ Paste into:**
genre_detection/

**🌍 Regional Detection**

**From:**
AI_Music_Data/models/regional_detection/region_model.pkl

**➡ Paste into:**
backend/regional_detection/

**🧾 Plagiarism Detection**

**From:**
AI_Music_Data/models/plagiarism_detection/feature_database.pkl

**➡ Paste into:**
backend/plagiarism_detection/



## 🔹 2. Song Database (REQUIRED ✅)

**Copy:**
AI_Music_Data/plagiarism_detection_database/song_database/

**➡️ into:**
AI_Music_Intelligence/backend/song_database/

**👉 Used for:**
* Plagiarism Detection

  

## 🔹 3. Backend Uploads (OPTIONAL ⚠️)

**Copy:**
AI_Music_Data/backend_uploads/

**➡️ into:**
AI_Music_Intelligence/backend/uploads/



## 🔹 4. Datasets (OPTIONAL ⚠️)

These are only needed if you want to retrain models:

* emotion_detection_dataset
* voice_emotion_detection_dataset
* regional_detection_dataset
* genre_detection_dataset

**👉 Not required for normal execution**


# 🧠 Important Notes

* ✅ Models are pre-trained
* ❌ No need to retrain
* ✅ song_database is required for system to work
* ❌ Do not change folder names


# ▶️ Run the Project

cd backend
python app.py


# 🧪 How It Works

1. User uploads/records audio
2. System performs:

   * Speech → Text (sentiment analysis)  
   * Emotion Detection 
   * Genre Detection
   * Regional Detection
   * Plagiarism Check
   * Song Recommendation


# ⚠️ Common Errors

## ❌ Models not loading

**➡️ Check:**
backend/models/


## ❌ Plagiarism / Recommendation not working

**➡️ Check:**
backend/song_database/


## ❌ App not starting

➡️ Run inside backend:
cd backend
python app.py


# 📌 Final Notes

* Keep folder structure exact
* Works online after setup
  

# 👩‍💻 Author
**Shaziya Ansari**
**AI Music Intelligence Project**
