import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14, 50)

while True:
    pwm.start(0.01)
    sleep(0.7)
    pwm.start(15)
    sleep(1)
    pwm.start(0.01)
    sleep(0.7)
    pwm.start(15)
    sleep(1)
    pwm.start(6)
    sleep(0.7)   
    break

