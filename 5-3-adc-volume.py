import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT, initial = 0)
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

    return elem
        
def leds(code):
    if (code >= 0) & (code < 32):
            GPIO.output(led, 0)
    else:
        p = int(code/32)
        k = 2**p - 1
        GPIO.output(led, dec2bin(k))        


try:
    while True:
        code = adc()
   
        leds(code)

        vol = code * 3.3/256
        print("bincode = ", dec2bin(code),"code = ", code, "\nvoltage = ", vol)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

