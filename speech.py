# v.2, added csv and exit command.
import speech_recognition as sr
from datetime import datetime
import csv


device_name = input("Device name: ")

while True:
	r = sr.Recognizer()
	mic = sr.Microphone()

	with mic as source:
		r.adjust_for_ambient_noise(source)

		time = datetime.now().strftime('%H:%M:%S')
		
		print("\n",time, "Say something:")

		audio = r.listen(source)

		try:
			words = r.recognize_google(audio, language="th-TH")
			print(words)
			with open('speech_timestamp.csv', 'a', encoding='utf-8') as f:
				fw = csv.writer(f)
				data = [time, words, device_name]
				fw.writerow(data)

			if words == "ออก":
				print("Goodbye.")
				break

		except Exception as e:
			print("Error", e)

