# In AI, data is often represented as vectors (1D arrays) and matrices (2D arrays).

# Images → matrices of pixel values
# Word embeddings → vectors of numbers
# Neural networks → matrix multiplications at every layer

# Neural networks: Every layer is a matrix multiplication between inputs and weights.
# Transformers: Attention mechanisms rely heavily on dot products.
# PCA & dimensionality reduction: Use eigenvectors and eigenvalues.

import numpy as np

# Vectors
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("Dot product:", np.dot(vector_a, vector_b))

# Matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix multiplication:\n", np.dot(matrix_a, matrix_b))