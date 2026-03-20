import numpy as np

A = np.array([1, -2, 3, 4, 5, 6, 7, 1, 9]).reshape(3, 3)
b = np.array([1, 2, 3])

c = np.linalg.solve(A, b)
print(c)

d = np.dot(A, c)
print(d)

e = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13]).reshape(3, 3)
f = np.linalg.solve(A, e)
print(f)

g = np.dot(A, f)
print(g)

h, i = np.linalg.eig(A)
print(h)
print("\n",i)

j = np.linalg.inv(A)
k = np.linalg.det(A)
print(j)
print(k)

l = np.linalg.norm(A, 1)
m = np.linalg.norm(A, 2)
n = np.linalg.norm(A, np.inf)
print(l)
print(m)
print(n)

