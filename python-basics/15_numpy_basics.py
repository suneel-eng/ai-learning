# NumPy is the engine behind AI math
# powering matrix operations, linear algebra, and fast computations.
# It’s used in everything from data preprocessing to neural network training.

# NumPy (Numerical Python) is a library for working with arrays, matrices, and numerical functions.
import numpy as np

# Creating arrays
arr1d = np.array([ 1, 2, 3, 4, 5 ]) # 1D array
print(arr1d)

arr2d = np.array([[ 1, 2, 3 ], [ 4, 5, 6 ]]) # 2D array
print(arr2d)

# Array operations
array1 = np.array([ 1, 2, 3 ])
array2 = np.array([ 4, 5, 6 ])

print(array1 + 10) # Add 10 to each element
print(array2 * 2)  # Multiply each element by 2

# Element-wise addition
array_sum = array1 + array2
print(array_sum)

# Element-wise multiplication
array_product = array1 * array2
print(array_product)

# Useful functions
print(np.zeros((2, 3))) # 2x3 array of zeros
print(np.ones((3, 2)))  # 3x2 array of ones
print(np.eye(3))        # 3x3 identity matrix

# Array statistics
data = np.array([1, 2, 3, 4, 5])
print(np.mean(data))   # Mean
print(np.median(data)) # Median
print(np.std(data))    # Standard deviation
print(np.sum(data))    # Sum
print(np.min(data))    # Minimum
print(np.max(data))    # Maximum

matrix = np.array([[1, 2], [3, 4]])
print("Sum:", np.sum(matrix))
print("Transpose:\n", matrix.T)
