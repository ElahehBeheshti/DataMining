def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]  # backtrack

def combine(data, start, index, length, curr):
    if index == length:
        print(''.join(curr))
        return
    for i in range(start, len(data)):
        curr[index] = data[i]
        combine(data, i + 1, index + 1, length, curr)

# Define the list
elements = list('ABCDE')

# All permutations
print("Permutations:")
permute(elements, 0, len(elements))

# Combinations of length 3
print("\nCombinations of Length 3:")
combine(elements, 0, 0, 3, [None]*3)
