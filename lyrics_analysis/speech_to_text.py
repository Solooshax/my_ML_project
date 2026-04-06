import speech_recognition as sr
from pydub import AudioSegment
from langdetect import detect
import os


def convert_speech_to_text(audio_path):

    wav_path = audio_path.replace(".mpeg", ".wav").replace(".mp3", ".wav")

    sound = AudioSegment.from_file(audio_path)
    sound.export(wav_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio_data = recognizer.record(source)

    try:
       text = recognizer.recognize_google(audio_data, language="en-US")

       print("TRANSCRIPT:", text)

       return text

    except Exception as e:
        print("Speech error:", e)
        return "could not understand audio" 

    