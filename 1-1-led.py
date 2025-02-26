"""создать скрипт 5-3-adc-volume.py
выполнить пункты из предыдущего задания
в блоке try:
в бесконечном цикле вызывать функцию adc()
преобразовать возвращаемое значение и выдать его на leds при помощи функции c прошлого занятия
обратите внимание, что при напряжении 0В все светодиоды погашены, при напряжении 3.3В все светодиоды должны гореть, при 1.67В должны гореть 4 светодиода из 8
проверить работу с использованием АЦП из первой задачи
проверить работу с использованием АЦП из второй задачи"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

"""def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        dac_val = dec2bin(k)
        GPIO.output(dac, dac_val)
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 0:
            k -= 2**i
    return k"""

def adc():
    j = 0
    for i in range(7, -1, -1):
        j = j + 2**i
        time.sleep(0.0014)
        GPIO.output(dac, dec2bin(j))
        if GPIO.input(comp) == 1:
            return j-2**i

def Volume(val):
    val = int(val/256*3.3) #vol
    arr = [0]*8            #00000000
    for i in range(val - 1):
        arr[i] = 1
    return arr

try:
    while True:
        i = adc()  #code
        if i:
            volume_val = Volume(i)
            GPIO.output(led, volume_val)
            print(int(i/256*10))
            
            
"""try:
    while True:
        code = adc()
        vol = code * 3.3/256
        print(code, vol)"""

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
