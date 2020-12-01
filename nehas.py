import speech_recognition as s
sr=s.Recognizer()
print("i am listening..........")

with s.Microphone() as m:
    audio=sr.listen(m)
    text=sr.recognize_google(audio,language='eng-in')
    print(text)