import json
def fibonacci(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    i = 0
    while i < n:
        yield (i, a)
        a, b = b, a + b
        i += 1


N = int(input("Enter a number: "))
fib_series = dict(fibonacci(N))
print(json.dumps(fib_series))
