import numpy as np
from scipy import stats

data = [ 10, 12, 23, 23, 16, 23, 21, 16 ]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("25th Percentile:", np.percentile(data, 25))