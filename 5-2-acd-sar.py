import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=0)
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


print("до try")

try:
    meas_data = []
    start_time = time.time()
    decod = 0

    print("до 1")

    GPIO.output(troyka, 1)      #зарядка кондера
    while (decod <= 206):
        decod = adc()
        print(decod)
        meas_data.append(decod)     # добавление новых данных в лист 
 
    print("до 0")

    GPIO.output(troyka, 0)      #разрядка кондера
    while (decod >= 178):
        decod = adc()
        print(decod)
        meas_data.append(decod)     # добавление новых данных в лист  

    print("до time")

    end_time = time.time()
    experiment_time = end_time - start_time     # продолжительность эксперимента

    print("до grafic")

    plt.plot(meas_data)     #график
    plt.show()

    print("до txt")

    meas_data_str = [str(item) for item in meas_data]

    with open("data.txt", "w") as outfile:                 #сохраняем значения data в data.txt
        outfile.write("\n".join(meas_data_str))


    #set = []

    frequency = str(len(meas_data)/experiment_time)
    step = str(3.3 / 256)
    intfr = len(meas_data)/experiment_time
    period = 1 / intfr

    with open("nsettings.txt", "w") as f:
        f.write(frequency)
        f.write("\n")
        f.write(step)

    print(experiment_time, period, float(frequency), float(step))


finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()



181
181
181
181
181
179
179
179
179
179
179
179
179
179
179
177
до time
до grafic
до txt
11.34979248046875 0.07138234264445754 14.009066709687827 0.012890625
b01-304@raspberrypi:~/Desktop/Scripts $  cd /home/b01-304/Desktop/Scripts ; /usr/bin/env /bin/python3 /opt/vscode/extensions/ms-python.python-2021.10.1365161279/pythonFiles/lib/python/debugpy/launcher 46773 -- /home/b01-304/Desktop/Scripts/7-1-measure.py 
до try
до 1
19
23
27
31
35
39
43
45
47
51
55
57
59
63
63
69
71
75
77
79
83
87
87
91
93
95
99
101
103
105
107
111
111
115
117
119
119
121
123
125
127
127
131
133
135
139
141
143
145
147
151
151
155
155
157
159
161
163
167
167
169
171
173
175
175
177
179
181
183
183
185
187
187
187
189
189
191
191
191
193
195
197
199
199
199
201
201
203
203
203
205
205
205
205
205
207
до 0
205
203
201
201
199
199
197
197
197
195
195
195
195
193
193
193
193
193
193
193
193
193
193
193
193
193
193
193
193
193
193
193
191
189
189
187
187
187
185
185
185
183
183
183
183
181
181
181
181
181
179
179
179
179
179
179
179
179
179
179
177
до time
до grafic
до txt
11.206303358078003 0.07137772839540128 14.009972332832433 0.012890625
