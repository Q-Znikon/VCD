import speech_recognition as sr

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say something")

        audio = r.listen(source)

        try:
            print(r.recognize_google(audio, language="th-TH"))

        except:
            print("Error")
