import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
xData = np.loadtxt("gaussian_data.txt")

# Add the histogram to the plot
n, bins, patches = plt.hist(xData, 100, range=[0,20], facecolor='g', alpha=0.75)

# Format the figure
plt.ylabel("Counts per bin",size=12)
plt.xlabel("$X$",size=12)
plt.title("Histogram of Gaussian Data")
plt.tight_layout()

# Display
plt.show()
