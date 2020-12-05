from gpiozero import Servo, Motor

from time import sleep

servo = Servo(14)
motor = Motor(21, 20)

while True:
    servo.min()
    sleep(4)
    motor.forward()
    sleep(0.2)
    motor.stop()
    sleep(0.2)
    motor.backward()
    sleep(0.2)
    motor.stop()

    servo.mid()
    sleep(4)
    servo.max()
    sleep(4)
    motor.forward()
    sleep(0.2)
    motor.stop()
    sleep(0.2)
    motor.backward()
    sleep(0.2)
    motor.stop()
gpio.cleanup()


