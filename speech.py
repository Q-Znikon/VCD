import speech_recognition as sr
from datetime import datetime

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        time = datetime.now().strftime('%H:%M:%S')

        print(time, "Say something:")

        audio = r.listen(source)

        try:
            words = r.recognize_google(audio, language="th-TH")
            print(time, words, "\n")

        except Exception as e:
            print(time, "Error", e, "\n")
