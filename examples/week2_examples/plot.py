import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# This is the fit function. Notice that it works
#   if x is a number, or a numpy array
def g(x,a,b):
    return a+b*x

# Read data from the file
xData, yData = np.loadtxt("linear_data.txt", delimiter=' ', unpack=True)

# Run the fit
pGuess=[-0.2,0.9] # this is my initial guess
pOpt, pCov = curve_fit(g, xData, yData, p0=pGuess)

# Calculate the individual parameter uncertainties
pUnc = np.sqrt(np.diag(pCov))

# Print out the results
print("The results of the fit")
print("  The intercept is {0:.3g} +/- {1:.3g}".format(pOpt[0],pUnc[0]))
print("  The slope is     {0:.3g} +/- {1:.3g}".format(pOpt[1],pUnc[1]))

# Make a plot
#    in case the data are sparse, I like having a regular dense
#    grid of x-values over which to plot any functions.
xVals=np.arange(-4,8,0.1) 
plt.plot(xData,yData,'o',color='black')
plt.plot(xVals,g(xVals,pGuess[0],pGuess[1]),'-',color='red')
plt.plot(xVals,g(xVals,pOpt[0],pOpt[1]),'-',color='blue')
plt.show()
