# Space Complexity:
# Space Complexity measures how the memory usage of an
# algorithm grows as the input size (n) increases.

import tracemalloc


# O(1) - Constant Space
# Uses a fixed amount of extra memory.
def constant_space(n):
    total = 0

    for i in range(n):
        total += i

    return total


# O(log n) - Logarithmic Space
# Recursive call stack grows logarithmically.
def logarithmic_space(n):
    if n <= 1:
        return 1

    return 1 + logarithmic_space(n // 2)


# O(n) - Linear Space
# Creates a list containing n elements.
def linear_space(n):
    new_list = [i for i in range(n)]
    return new_list


# O(n^2) - Quadratic Space
# Creates an n by n matrix.
def quadratic_space(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    return matrix


# Different input sizes for testing
sizes = [100, 500, 1000, 2000, 3000]

# Store algorithms in a dictionary
algorithms = {
    "O(1)": constant_space,
    "O(log n)": logarithmic_space,
    "O(n)": linear_space,
    "O(n^2)": quadratic_space,
}


# Measure memory usage for each algorithm
for name, function in algorithms.items():
    print(f"\nAlgorithm: {name}")

    for n in sizes:
        tracemalloc.start()

        # Execute the algorithm
        result = function(n)

        # Get peak memory usage
        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        # Display results
        print(f"Input Size: {n:4}, Peak Memory Usage: {peak / 1024:9.2f} KB")

        del result
