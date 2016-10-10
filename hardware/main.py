# import RPi.GPIO as GPIO
from firebase import firebase
import time
import datetime


# Firebase infos
FIREBASE_DATABASE_URL = 'https://break-manager-ac99b.firebaseio.com'
FIREBASE_DATABASE_NODE = '/moody/days/'

# Values infos
VALUE_HAPPY = "HAPPY"
VALUE_MEDIUM = "MEDIUM"
VALUE_SAD = "SAD"

# Setup GPIO
PIN_HAPPY = 18;
# pinCasual = 18;
# pinSad = 18;

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PIN_HAPPY, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Go !
def main():
	initFirebase()
	while True:
	    # state_happy = GPIO.input(PIN_HAPPY)
	    # if state_happy == False:
	    if True:
			print('Button Happy Pressed')

			value = VALUE_HAPPY
			day = datetime.date.today()
			now = datetime.datetime.now()
			postFirebase(value, day, now)

			time.sleep(0.5)


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


if __name__ == '__main__':
	main()