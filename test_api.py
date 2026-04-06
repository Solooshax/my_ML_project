import requests

url = "http://127.0.0.1:5000/detect-emotion"

files = {
"audio": open("emotion_detection/dataset/Actor_01/03-01-01-01-01-01-01.wav", "rb")
}

response = requests.post(url, files=files)

print(response.json())
