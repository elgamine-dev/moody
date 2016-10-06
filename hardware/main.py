import RPi.GPIO as GPIO
import time

pinHappy = 18;
# pinCasual = 18;
# pinSad = 18;

GPIO.setmode(GPIO.BCM)

GPIO.setup(pinHappy, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    state_happy = GPIO.input(pinHappy)
    if state_happy == False:
        print('Button Happy Pressed')
        time.sleep(0.5)