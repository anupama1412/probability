import matplotlib.pyplot as plt
import numpy as np

# Function to calculate theoretical gamma CDF
def theoretical_gamma_cdf(x, n):
    result = 1
    for i in range(1, n):
        result *= x / i
    return 1 - np.exp(-x) * result

# Read simulated data from a file (replace 'simulation_data.txt' with the actual filename)
data = np.loadtxt('output.txt')
x_values = data[:, 0]
simulated_probs = data[:, 1]

# Define the shape parameter 'n'
n = 5  # You can change this value according to your requirement

# Calculate theoretical CDF values for the given 'n'
theoretical_probs = [theoretical_gamma_cdf(n * x, n) for x in x_values]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, theoretical_probs, label='Theoretical CDF')
plt.scatter(x_values, simulated_probs, color='r', label='Simulated Probability', marker='o')
plt.xlabel('x')
plt.ylabel('CDF')
plt.title('Theoretical vs. Simulated Gamma CDF')
plt.legend()
plt.grid(True)
plt.show()

