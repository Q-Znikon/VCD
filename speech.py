# v.2
import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)

	while True:

		response = {
			"success": True,
			"error": None,
			"transcription": None
		}


		try:
			words = r.recognize_google(audio, language="th-TH")
		except sr.RequestError:
			response["success"] = False
			response["error"] = "API unavailable"
		except sr.UnknownValueError:
			response["error"] = "Unable to recognize speech"

		#return response
