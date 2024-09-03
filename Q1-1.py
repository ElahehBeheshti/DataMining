#1. Using Python Lists
import cProfile

# Define matrices using Python lists
A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

# Matrix Addition
def matrix_addition(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Matrix Multiplication
def matrix_multiplication(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Matrix Transpose
def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Profile the functions
def profile_list_operations():
    matrix_addition(A, B)
    matrix_multiplication(A, C)
    matrix_transpose(A)

cProfile.run('profile_list_operations()')
