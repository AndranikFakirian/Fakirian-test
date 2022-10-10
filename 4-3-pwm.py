import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup([22, 24], gpio.OUT)
gpio.setup(2, gpio.IN)
p1=gpio.PWM(22, 1000)
p2=gpio.PWM(24, 1000)
p1.start(0)
p2.start(0)
try:
    while True:
        d=int(input())
        p1.start(d)
        p2.start(d)
        uud=3.3*d/100
        print("Предполагаемое значение = {:.4f} В".format(uud))
finally:
    p1.stop()
    p2.stop()
    gpio.cleanup()
