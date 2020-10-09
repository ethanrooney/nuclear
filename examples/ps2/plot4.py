import matplotlib.pyplot as plt
import numpy as np

def R(E):
    return 1./(1.+E)

def T(E):
    return E/(1.+E)

xVals=np.arange(0,5,0.1)

plt.plot(xVals,R(xVals),'-r')
plt.plot(xVals,T(xVals),'-b')
plt.xlim(0,5)
plt.xlabel(r'Energy (in units of $m \alpha^2 /2\hbar^2$)',size=12)
plt.ylabel("Probability",size=12)
plt.text(3,0.65,"Transmission",color="blue",size=14)
plt.text(3,0.35,"Reflection",color="red",size=14)

#plt.show()
plt.savefig("delta_scatter.pdf")
