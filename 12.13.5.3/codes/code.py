import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters for the binomial distribution
n = 10  # Number of trials
p = 0.05  # Probability of success

p0 = binom.pmf(0, n, p)
p1 = binom.pmf(1, n, p)

print(f'P(X = 0) =', p0)
print(f'P(X = 1) =', p1)

print('Total probability =', p0+p1)
