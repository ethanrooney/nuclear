import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit

def fitfunc(x,a):
    return a*np.sin(np.absolute(x*m.pi/360.))

dataX,data05,data10,data15= np.loadtxt("data.txt", delimiter=' ', unpack=True,usecols=(0,1,2,3))

pOpt05,pCov05=curve_fit(fitfunc,dataX,data05)
pOpt10,pCov10=curve_fit(fitfunc,dataX,data10)
pOpt15,pCov15=curve_fit(fitfunc,dataX,data15)

plt.bar(dataX,data15,align="center",color="red",width=4)
plt.bar(dataX,data10,align="center",color="#00CC00",width=4)
plt.bar(dataX,data05,align="center",color="blue",width=4)
plt.plot(dataX,fitfunc(dataX,pOpt05[0]),'--w',lw=3)

plt.xlabel('Scattering Angle $\Theta$ [deg.]')
plt.ylabel('Cross section [units of side length]')
plt.xlim(-180,180)

plt.text(-35,0.002,'$b=0.5s$',color="blue",size=14)
plt.text(-60,0.003,'$b=1.0s$',color="#00CC00",size=14)
plt.text(-100,0.004,'$b=1.5s$',color="red",size=14)
plt.text(-160,0.0022,'$\sin(|\Theta/2|)$',color="white",size=14)

#plt.show()
plt.savefig("prob5_results.pdf")
