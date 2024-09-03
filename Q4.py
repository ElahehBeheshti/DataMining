import itertools

# Define the list
elements = ['A', 'B', 'C', 'D', 'E']

# Compute all permutations of the list
print("All Permutations:")
for perm in itertools.permutations(elements):
    print(''.join(perm))

# Compute all combinations of the list for length 3
print("\nCombinations of Length 3:")
for combo in itertools.combinations(elements, 3):
    print(''.join(combo))
