from scipy import stats
import numpy as np

sigma = 164.43
N = 50
mu = 4.56
I = stats.norm.interval(0.95, loc=mu, scale=sigma/np.sqrt(N))
print(I)
