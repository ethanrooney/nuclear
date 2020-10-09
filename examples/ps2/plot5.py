import matplotlib.pyplot as plt
import numpy as np


dataX,data02,data1,data5= np.loadtxt("scatter_data.txt", delimiter=' ', unpack=True,usecols=(0,1,2,3))

plt.yscale("log")
plt.ylim(1.E-4,1)
plt.plot(dataX,data02,'--r',label=r'$R$, $m=0.2$')
plt.plot(dataX,data1,'-r',label=r'$R$, $m=1$')
plt.plot(dataX,data5,'-.r',label=r'$R$, $m=5$')

plt.xlim(0,10)
plt.xlabel(r'$k$',size=12)
plt.ylabel("Probability",size=12)
plt.legend()

plt.savefig("prob5_results_log.pdf")

plt.yscale("linear")
plt.ylim(0,1)

plt.plot(dataX,1-data02,'--b',label=r'$T$, $m=0.2$')
plt.plot(dataX,1-data1,'-b',label=r'$T$, $m=1$')
plt.plot(dataX,1-data5,'-.b',label=r'$T$, $m=5$')
plt.legend()

#plt.show()
plt.savefig("prob5_results.pdf")
