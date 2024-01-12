from functools import reduce

# Generate Fibonacci series up to n using lambda function and map
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

# Limit the series up to 50
result = list(filter(lambda x: x <= 50, fibonacci_series(50)))

print(result)
