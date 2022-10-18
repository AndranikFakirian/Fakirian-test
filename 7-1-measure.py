import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt
leds=[21, 20, 16, 12, 7, 8, 25, 24] #Initializing raspberry pi
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)
gpio.setup(comp, gpio.IN)
def d2b (x): #Function which translates decimal into binary
    s=bin(x)[2:]
    p=[]
    for i in s:
        p.append(int(i))
    l=[]
    for i in range(0, 8-len(p)):
        l.append(0)
    return l+p
def adc (): #Function which takes voltage
    m=[0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(-7, 1):
        p=d2b(2**(-i))
        for j in range(0, 8):
            p[j]+=m[j]
        gpio.output(dac, p)
        time.sleep(0.01)
        a=gpio.input(comp)
        if a==1:
            m[7+i]=1
    s=0
    for i in m:
        s*=2
        s+=i
    return s
try:
    data=open("data.txt", 'w') #Initializing files
    settings=open("settings.txt", 'w')
    tbeg=time.time() #Take the time
    voltage1=[]
    gpio.output(troyka, 1) #Turning on the voltage and measuring voltage on the condenser
    while True:
        vol=adc()
        volv=3.3*vol/256
        voltage1.append(volv)
        gpio.output(leds, d2b(vol))
        print('{:.4f} V'.format(volv))
        if (vol>=249):
            break
    voltage2=[]
    gpio.output(troyka, 0) #Turning off the voltage and measuring voltage on the condenser
    while True:
        vol=adc()
        volv=3.3*vol/256
        voltage2.append(volv)
        gpio.output(leds, d2b(vol))
        print('{:.4f} V'.format(volv))
        if (vol<=0):
            break
    tend=time.time() #Take the time
    T=tend-tbeg #Calculate parameters
    Tof1=T/(len(voltage1)+len(voltage2))
    freq=1/Tof1
    quant=3.3/256
    pt=plt.subplot()
    pt.plot(voltage1+voltage2) #Build plot
    pt.set(title='RC voltage')
    data.write('Increasing voltage:\n') #Record data to files
    for i in voltage1:
        data.write('{:.4f} V\n'.format(i))
    data.write('Decreasing voltage:\n')
    for i in voltage2:
        data.write('{:.4f} V\n'.format(i))
    data.close()
    settings.write('Discr. frequency = {:.4f} Hz\n'.format(freq))
    settings.write('Step of quant. = {:.4f} V'.format(quant))
    settings.close()
    print('Time of exp. = {:.4f} s'.format(T)) #Print calculated parameters
    print('Period of 1 meas. = {} s'.format(Tof1))
    print('Av. discr. frequency = {:.4f} Hz'.format(freq))
    print('Step of quant. = {:.4f} V'.format(quant))
    plt.show() #Show plot
finally:
    gpio.output(dac, d2b(0)) #Turning off raspberry pi
    gpio.output(leds, d2b(0))
    gpio.output(troyka, 0)
    gpio.cleanup()