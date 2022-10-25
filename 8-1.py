import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import numpy as nm
dat=nm.loadtxt('data.txt', dtype=float)
with open ('settings.txt', 'r') as st:
    freqs=st.readline()
    quants=st.readline()
st.close()
freq=float(freqs[:len(freqs)-1])
quant=float(quants)
len = dat.size
dm=nm.argmax(dat)
dat=3.3/248*dat
time=nm.arange(len)
time=time*freq
fig, ax = plt.subplots()
ax.plot(time, dat, linestyle='-', linewidth = 1,  color= 'crimson', label='V(t)')
ax.legend(loc = 0)
tim=[]
da=[]
for i in range(0, len, 50):
    tim.append(time[i])
    da.append(dat[i])
ax.scatter(tim, da, s=10, c='crimson')
ax.set_ylabel('Voltage, V')
ax.set_xlabel('Time, s')
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(tic.MultipleLocator(0.4))
ax.yaxis.set_major_locator(tic.MultipleLocator(0.5))
ax.xaxis.set_major_locator(tic.MultipleLocator(2))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, color='grey')
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, color='grey')
ax.set_xlim([0, 14])
ax.set_ylim([0.0, 3.5])
ax.set_title('Charging and discharging of capacitor in RC-circuit', loc='center', pad=10)
t1=time[dm]
t2=time[len-1]-time[dm]
ax.text(8, 2.2, 'Charging time = {:.2f} s'.format(t1))
ax.text(8, 1.7, 'Discharging time = {:.2f} s'.format(t2))
plt.show()
fig.savefig('plot.svg')