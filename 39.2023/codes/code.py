import math
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate theoretical Gamma CDF values
def gamma_cdf(x, alpha, beta):
    return 1 - math.exp(-pow(x / beta, alpha))

# Parameters
alpha = 2.0
beta = 0.5
start_x = 0.1
end_x = 5.0
step = 0.1

# Generate x values
x_values = np.arange(start_x, end_x + step, step)

# Calculate theoretical Gamma CDF values
theoretical_cdf_values = [gamma_cdf(x, alpha, beta) for x in x_values]

# Read simulated empirical probabilities from the C code output
data = np.loadtxt('output.txt')
simulated_probabilities = data

# Plot theoretical vs simulated Gamma CDF
plt.figure(figsize=(8, 6))
plt.plot(x_values, theoretical_cdf_values, label='Theoretical Gamma CDF', color='blue', linewidth=2)
plt.plot(x_values, simulated_probabilities, label='Simulated Gamma CDF', color='red', marker='o', linestyle='None', markersize=5)
plt.xlabel('x')
plt.ylabel('CDF Value')
plt.title('Theoretical vs Simulated Gamma CDF')
plt.legend()
plt.grid(True)
plt.show()

