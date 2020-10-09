#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

f_s = 10  # Sampling rate, or number of measurements per second

data = pd.read_csv('../p5_data.txt', sep=' ', header=None)

t=data[0]
x=np.sqrt(data[1])



fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_ylabel('F(q)')
ax.set_xlabel('q')


from scipy import fftpack

X = fftpack.fft(x)/(2*math.pi)**3 
freqs = fftpack.fftfreq(len(x))*2

print sum(np.abs(X))

fig, fftax = plt.subplots()

fftax.stem(freqs, np.abs(X))
fftax.set_xlabel('r')
fftax.set_ylabel('Charge Density')
fftax.set_xlim(0, 1 )
fftax.set_ylim(0, .25 )

plt.show(fftax)
