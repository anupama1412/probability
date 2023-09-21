import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range of values for Z
z_values = np.linspace(-3, 3, 1000)  # Choose an appropriate range

# Calculate the CDF values for each Z value
cdf_values = norm.cdf(z_values)

# Plot the CDF
plt.plot(z_values, cdf_values)
plt.xlabel('Z')
plt.ylabel('CDF(Z)')
plt.title('CDF of the Standard Normal Distribution')
plt.grid(True)
plt.savefig('../figs/fig.png')


