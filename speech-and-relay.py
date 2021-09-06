# v.1
import speech_recognition as sr
from datetime import datetime
import RPi.GPIO as GPIO

### GPIO numbers ###
lamp1 = 8
lamp2 = 10

### Board mode ###
GPIO.setmode(GPIO.BOARD)

### setup GPIO pins ###
GPIO.setup(lamp1, GPIO.OUT)
GPIO.setup(lamp2, GPIO.OUT)

##### function for pins #####
### lamp1 ###
def channel1_0(pin):
    GPIO.output(pin, GPIO.HIGH)
def channel1_1(pin):
    GPIO.output(pin, GPIO.LOW)
### lamp 2 ###
def lamp2_off(pin):
    GPIO.output(pin, GPIO.HIGH)
def lamp2_on(pin):
    GPIO.output(pin, GPIO.LOW)
#############################

### set startup to off ###
channel1_0(lamp1)
lamp2_off(lamp2)

while True: # loop script 
	r = sr.Recognizer()

	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		time = datetime.now().strftime('%H:%M:%S')
		print(time, "Say something:")
		audio = r.listen(source)

		try:
			words = r.recognize_google(audio, language="th-TH")
			print(time, words)

			### lamp 1 ###
			if words == ("เปิดไฟ 1"):
				lamp1_on(lamp1)
				print(time, "Relay1 on", "\n")
			if words == ("ปิดไฟ 1"):
				channel1_0(lamp1)
				print(time, "Relay1 off", "\n")

			### lamp 2 ###
			if words == ("เปิดไฟ 2"):
				lamp2_on(lamp2)
				print(time, "Relay2 on", "\n")
			if words == ("ปิดไฟ 2"):
				lamp2_off(lamp2)
				print(time, "Relay2 off", "\n")

		except Exception as e:
			print(time, "Error", e, "\n")
