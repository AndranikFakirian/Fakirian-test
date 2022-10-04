import RPi.GPIO as gpio
import time
dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[21, 20, 16, 12, 7, 8, 25, 24]
comp=4
troyka=17
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
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
def enter ():
    s=adc()
    g=round(s/32)
    p=[]
    for i in range(0, 8):
        if i<g:
            p.append(1)
        else:
            p.append(0)
    return p[::-1]
try:
    while True:
        gpio.output(leds, enter())
finally:
    gpio.output(dac+leds, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()