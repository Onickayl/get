import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

class ValidationError(Exception):
    pass

def num_value(a):
    if a < 0:
        raise ValidationError('Number < 0')
    elif a > 255:
        raise ValidationError('Number > 255')
    return True


try:
    while True:
        print("Enter number from 0 to 255: ")
        a = int(input())
        num_value(a)
        
        GPIO.output(dac, dec2bin(a))
        vol = a * (3.3 / 256)
        print("voltage = ", vol)
        
except ValueError:
    print("That's not an int or number!")
        
except ValidationError as e:
    print(e)                      
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    