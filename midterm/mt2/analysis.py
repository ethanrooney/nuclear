import math as m
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import cmath
mu=470.
E=[0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0,20.0,50.0,100.0]
hbar=197.0
l=0
mu=470.
t= np.linspace(0,np.pi,180)

def pl(x,l):

    return 1

def f2(x,d0,d1,d2,d3,d4):
    p = [1.,x,0.5*(3.*x**2.-1.),0.5*(5.*x**3.-3.*x),1./8.*(35.*x**4.-30.*x**2.+3.)]
    d = [d0,d1,d2,d3,d4]
    v = np.linspace(0.,0.,len(x))
    vreal=np.linspace(0.,0.,len(x))
    vimag=np.linspace(0.,0.,len(x))
    for l in range(0,len(p)):
        vreal+=(2.*l+1.)*np.sin(d[l])*np.cos(x)*np.cos(d[l])*p[l]
        vimag+=(2.*l+1.)*np.sin(d[l])*np.cos(x)*np.sin(d[l])*p[l]
    return (vreal**2+vimag**2)/k**2

for i in range(1,16):
    files = str(i)+".txt"
    data=pd.read_csv(files, sep='\s', header=None, engine='python')
    k=np.sqrt(2*mu*E[i])/hbar
    x=data[0]/180.*np.pi
    y=data[1]
    e=data[2]
    pop, pot = curve_fit(f2,x.values, y.values)
    t=np.linspace(0,np.pi,100)
    plt.errorbar(x,y,yerr=e, fmt='o')
    x1=np.linspace(0,np.pi,100)
    y1=f2(x1,pop[0], pop[1], pop[2], pop[3], pop[4])
    plt.plot(x1,y1)
    plt.show()




#
#    vreal=np.linspace(0.,0.,len(x))
#    vimag=np.linspace(0.,0.,len(x))
#    vreal+=(2.*0.+1.)*np.sin(d0)*np.cos(x)*np.cos(d0)*p[0]
#    vreal+=(2.*1.+1.)*np.sin(d1)*np.cos(x)*np.cos(d1)*p[1]
#    vreal+=(2.*2.+1.)*np.sin(d2)*np.cos(x)*np.cos(d2)*p[2]
#    vreal+=(2.*3.+1.)*np.sin(d3)*np.cos(x)*np.cos(d3)*p[3]
#    vreal+=(2.*4.+1.)*np.sin(d4)*np.cos(x)*np.cos(d4)*p[4]
#    vimag+=(2.*0.+1.)*np.sin(d0)*np.cos(x)*np.sin(d0)*p[0]
#    vimag+=(2.*1.+1.)*np.sin(d1)*np.cos(x)*np.sin(d1)*p[1]
#    vimag+=(2.*2.+1.)*np.sin(d2)*np.cos(x)*np.sin(d2)*p[2]
#    vimag+=(2.*3.+1.)*np.sin(d3)*np.cos(x)*np.sin(d3)*p[3]
#    vimag+=(2.*4.+1.)*np.sin(d4)*np.cos(x)*np.sin(d4)*p[4]
