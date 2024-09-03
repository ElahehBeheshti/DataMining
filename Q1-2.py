#2. Using NumPy
import cProfile
import numpy as np

# Define matrices using NumPy arrays
A_np = np.array([[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]])
B_np = np.array([[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]])
C_np = np.array([[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]])

# Matrix Addition
def matrix_addition_np(A, B):
    return A + B

# Matrix Multiplication
def matrix_multiplication_np(A, B):
    return np.dot(A, B)

# Matrix Transpose
def matrix_transpose_np(A):
    return A.T

# Profile the functions
def profile_numpy_operations():
    matrix_addition_np(A_np, B_np)
    matrix_multiplication_np(A_np, C_np)
    matrix_transpose_np(A_np)

cProfile.run('profile_numpy_operations()')
