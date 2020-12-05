from gpiozero import Motor

from time import sleep

motor = Motor(20, 21)

while True:
    motor.forward()
    sleep(0.25)
    motor.stop()
    sleep(1)
    motor.backward()
    sleep(0.25)
    motor.stop()
gpio.cleanup()

