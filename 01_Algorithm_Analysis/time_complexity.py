# Time Complexity:
# Time Complexity measures how the execution time of an
# algorithm grows as the input size (n) increases.

import time


# O(1) - Constant Time
# Execution time does not depend on input size.
def constant_time(n):
    return n + 1


# O(log n) - Logarithmic Time
# The input size is divided by 2 in each iteration.
def logarithmic_time(n):
    while n > 1:
        n = n // 2


# O(n) - Linear Time
# The loop runs n times.
def linear_time(n):
    for i in range(n):
        pass


# O(n^2) - Quadratic Time
# Two nested loops.
# Total operations = n * n.
def quadratic_time(n):
    for i in range(n):
        for j in range(n):
            pass


# Different input sizes for testing
sizes = [100, 500, 1000, 2000, 3000]

# Store algorithms in a dictionary
algorithms = {
    "O(1)": constant_time,
    "O(log n)": logarithmic_time,
    "O(n)": linear_time,
    "O(n^2)": quadratic_time,
}


# Measure execution time for each algorithm
for name, function in algorithms.items():
    print(f"\nAlgorithm: {name}")

    for n in sizes:
        start = time.perf_counter()

        # Execute the algorithm
        function(n)

        end = time.perf_counter()

        elapsed_time = end - start

        # Display results
        print(f"Input Size: {n:4}, Execution Time: {elapsed_time:9.8f} seconds")
