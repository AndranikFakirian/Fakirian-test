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
    for i in range(1, 256):
        p=d2b(i)
        gpio.output(dac, p)
        time.sleep(0.007)
        a=gpio.input(comp)
        if a==0:
            return i-1
    return 255
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