import numpy as np
from scipy import stats

data = [ 10, 12, 23, 23, 16, 23, 21, 16 ]

# Measures of central tendency
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)

# Measures of dispersion
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Range:", np.ptp(data))
print("25th Percentile:", np.percentile(data, 25))
print("Interquartile Range (IQR):", stats.iqr(data))