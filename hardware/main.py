import RPi.GPIO as GPIO
from firebase import firebase
import config
import time
import datetime


# Firebase infos
FIREBASE_DATABASE_URL = config.FIREBASE_DATABASE_URL
FIREBASE_DATABASE_NODE = config.FIREBASE_DATABASE_NODE

# Values infos
VALUE_HAPPY = "HAPPY"
VALUE_MEDIUM = "MEDIUM"
VALUE_SAD = "SAD"

# Setup GPIO
PIN_HAPPY = 22; # Pin 15
PIN_MEDIUM = 27; # Pin 13
PIN_SAD = 17; # Pin 11

PIN_LED = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_HAPPY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_MEDIUM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_SAD, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(PIN_LED,GPIO.OUT)
GPIO.output(PIN_LED,GPIO.HIGH)

# Go !
def main():
	initFirebase()
	while True:
	    state_happy = GPIO.input(PIN_HAPPY)
	    state_medium = GPIO.input(PIN_MEDIUM)
	    state_sad = GPIO.input(PIN_SAD)

	    if state_happy == False:
			onButtonPressed(VALUE_HAPPY)
	    if state_medium == False:
			onButtonPressed(VALUE_MEDIUM)
	    elif state_sad == False:
			onButtonPressed(VALUE_SAD)


def initFirebase():
	global firebase
	firebase = firebase.FirebaseApplication(FIREBASE_DATABASE_URL, None)

def postFirebase(value, day, timestamp):
	new_mood = {
		"value" : value,
		"day" : str(day),
		"ts" : str(timestamp)
	};

	result = firebase.post(FIREBASE_DATABASE_NODE+ str(day), new_mood)
	print result

def onButtonPressed(value):
	print('Button ' + value + ' Pressed')
	GPIO.output(PIN_LED,GPIO.LOW)

	day = datetime.date.today()
	now = datetime.datetime.now()
	postFirebase(value, day, now)
	
	GPIO.output(PIN_LED,GPIO.HIGH)
	# time.sleep(0.5)

if __name__ == '__main__':
	try:
		main()
	except:
		print 'Terminating'
		GPIO.output(PIN_LED,GPIO.LOW)
