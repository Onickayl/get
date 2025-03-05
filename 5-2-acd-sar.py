import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    elem = 128
    t = 0.01
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 64
    else:
        elem = elem + 64
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 32
    else:
        elem = elem + 32
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 16
    else:
        elem = elem + 16
    
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 8
    else:
        elem = elem + 8
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 4
    else:
        elem = elem + 4
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 2
    else:
        elem = elem + 2
        
    GPIO.output(dac, dec2bin(elem))
    time.sleep(t)
    if GPIO.input(comp) == 1:
        elem = elem - 1
    else:
        elem = elem + 1
    
        
        
try:
    while True:
        code = adc()
        vol = code * 3.3/256
        print(code, vol)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()