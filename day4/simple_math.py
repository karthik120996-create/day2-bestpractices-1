import numpy as np

def fibonacci(n):
    a = 0
    b = 1

    while b <= n:
        a, b = b, a + b
    return b
print(fibonacci(20))