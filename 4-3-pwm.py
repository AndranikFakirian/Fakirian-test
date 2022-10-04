import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup([22, 24], gpio.OUT)
gpio.setup(2, gpio.IN)
p1=gpio.PWM(22, 50)
p2=gpio.PWM(24, 50)
p1.start(0)
p2.start(0)
r=1000
w=2*3.14159265358979323846*50
c=10**(-5)
rc=1/(w*c)
z=(r*r+rc*rc)**(1/2)
u=3.3*rc/z
ud=u/(2**(1/2))
try:
    while True:
        d=int(input())
        p1.start(d)
        p2.start(d)
        uud=ud*d/100
        print("Предполагаемое значение = {:.4f} В".format(uud))
finally:
    p1.stop()
    p2.stop()
    gpio.cleanup()