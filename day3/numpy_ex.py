import numpy as np
a = np.zeros(10)
a[4] = 1
print(a)

b = np.arange(10, 50)
print(b)

c = b[::-1]
print(c)

d = np.arange(0, 9).reshape(3, 3)
print(d)

e = np.array([1, 2, 0, 0, 4, 0])
e1 = e.nonzero()
print(e1)

f = np.random.rand(30)
f_mean = f.mean()
print(f_mean)

g = np.array([1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1]).reshape(4, 4)
print(g)

h = np.zeros((8, 8))
h[1::2, ::2] = 1
h[::2, 1::2] = 1
print(h)

i = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print(i)

j = np.arange(11)
j1 = (j > 3) & (j < 8)
j[j1] = -j[(j1)]
print(j)

k = np.random.rand(10)
k1 = k.sort()
print(k)

l1 = np.random.randint(0, 2, 5)
l2 = np.random.randint(0, 2, 5)
l = np.equal(l1, l2)
print(l)

m = np.arange(10, dtype=np.int32)
print(m)
m **= 2
print(m)

n1 = np.arange(9).reshape(3, 3)
n2 = n1.T
n3 = n1.dot(n2)
n = np.diag(n3)
print(n)