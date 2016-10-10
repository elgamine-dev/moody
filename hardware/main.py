# import RPi.GPIO as GPIO
import time
from firebase import firebase
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
	    if true:
			print('Button Happy Pressed')

			value = VALUE_HAPPY
			day = datetime.date.today()
			now = datetime.datetime.now()
			postFirebase(value, day, now)

			time.sleep(0.5)


def initFirebase():
	firebase = firebase.FirebaseApplication(FIREBASE_DATABASE_URL, None)

def postFirebase(value, day, timestamp):
	new_mood = {
		"value" : "HAPPY",
		"day" : str(today),
		"ts" : str(now)
	};

	result = firebase.post(FIREBASE_DATABASE_NODE+ str(today), new_mood)
	print result


if __name__ == '__main__':
	main()