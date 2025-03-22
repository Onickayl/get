import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)        #GPIO пин
GPIO.setup(22, GPIO.OUT)        #led


p = GPIO.PWM(26, 1000) 
q = GPIO.PWM(22, 1000) 
p.start(0)
q.start(0)
try:
    while True:
        print("Enter duty cycle: ")
        dc = int(input())
        p.ChangeDutyCycle(dc)
        q.ChangeDutyCycle(dc)
        time.sleep(0.1)

        vol = dc * (3.3 / 100)
        print("voltage = ", vol)

finally:
    p.stop()
    GPIO.output(26, 0)
    GPIO.output(22, 0)
    GPIO.cleanup()
