import RPi.GPIO as gpio
import time
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
def d2b (x):
    s=bin(x)[2:]
    p=[]
    for i in s:
        p.append(int(i))
    l=[]
    for i in range(0, 8-len(p)):
        l.append(0)
    return l+p
def adc ():
    m=[0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(-7, 1):
        p=d2b(2**(-i))
        for j in range(0, 8):
            p[j]+=m[j]
        gpio.output(dac, p)
        time.sleep(0.1)
        a=gpio.input(comp)
        if a==1:
            m[7+i]=1
    s=0
    for i in m:
        s*=2
        s+=i
    return s
try:
    while True:
        c=adc()
        u=3.3*c/256
        print("Цифровое значение = {0}. Напряжение = {1}.".format(c, u))
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()