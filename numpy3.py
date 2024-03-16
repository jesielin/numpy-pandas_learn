import numpy as np

a = np.array([10, 20, 30, 40])

b = np.arange(4)

print(a, b)

print(a + b)
print(a - b)
print(a * b)

print(b > 3)
print(b < 3)
print(b == 3)

a = np.array([[1, 2], [3, 4]])
b = np.arange(4).reshape(2, 2)
print(a, b)

print(a * b)
print(np.dot(a, b))

# a = np.arange(24).reshape((2,3,4))
a = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11]],

              [[12, 13, 14, 15],
               [16, 0, 18, 19],
               [20, 21, 22, 23]]])
print(a)
print(np.min(a, axis=2))
print(np.max(a, axis=0))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
print(np.sum(a, axis=2))
