import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#Number of items
n = 10 
#Probability of a defective item
p = 0.05
#k is the possible number of defective items
k_values = list(range(n+1))
#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)
z=y[0]+y[1]
print(z)   #printing the probability of the number of defective item being atmost 1



