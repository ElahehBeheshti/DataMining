import numpy as np

# I. Create a List
numbers = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
print("II. Iterate using a for loop:")
for number in numbers:
    print(number)

# III. Iterate using for loop and range
print("\nIII. Iterate using for loop and range:")
for i in range(len(numbers)):
    print(numbers[i])

# IV. List Comprehension
print("\nIV. List Comprehension:")
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# V. Enumerate
print("\nV. Enumerate:")
for index, number in enumerate(numbers):
    print(f"Index {index}: {number}")

# VI. Iter function and next function
print("\nVI. Iter function and next function:")
num_iter = iter(numbers)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

# VII. Map function
print("\nVII. Map function:")
def square(x):
    return x * x
squared_numbers_map = list(map(square, numbers))
print(squared_numbers_map)

# VIII. Using zip
print("\nVIII. Using zip:")
names = ["Number One", "Number Two", "Number Three", "Number Four", "Number Five", 
         "Number Six", "Number Seven", "Number Eight", "Number Nine", "Number Ten"]
for name, number in zip(names, numbers):
    print(f"{name}: {number}")

# IX. Using NumPy Module
print("\nIX. Using NumPy Module:")
np_numbers = np.array(numbers)
print("NumPy Array:", np_numbers)
print("Array Mean:", np.mean(np_numbers))
print("Array Standard Deviation:", np.std(np_numbers))
