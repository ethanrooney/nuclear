import math as m
import cmath as cm
import numpy as np

def V(x):
    return (3.-2*x-x*x)*m.exp(x)

def rightPsi(x,k):
    return cm.exp(complex(0.,k*x))

step=0.001

def R(k,mass):
    lastPsi=rightPsi(1.+step,k)
    thisPsi=rightPsi(1.,k)

    x=1.
    while (x>0.):
        nextPsi = -lastPsi + 2.*thisPsi*(1. + step*step*(mass*V(x) - k*k/2.))

        x-=step
        lastPsi=thisPsi
        thisPsi=nextPsi

    psi0=thisPsi
    psiPrime0=(lastPsi-thisPsi)/step

    A=(complex(0,k)*psi0 - psiPrime0)/(complex(0,k)*psi0 + psiPrime0)
    mag,phase=cm.polar(A)
    return mag*mag

for k in np.arange(0.1,10,0.1):
    print(k,end=' ')
    #for mass in np.arange(0.5,2,0.5):
    for mass in [0.2,1,5]:
        print(R(k,mass),end=' ')
    print()
