import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

#/////шиииииииииииииииим
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while True:
        print("Enter duty cycle: ")
        dc = int(input())
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()