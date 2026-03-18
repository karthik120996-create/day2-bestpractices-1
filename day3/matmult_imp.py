import numpy as np

N = 250

X = np.random.randint(0, 100, size=(N, N))
Y = np.random.randint(0, 100, size=(N, N+1))

Z = np.dot(X, Y)

print(Z)