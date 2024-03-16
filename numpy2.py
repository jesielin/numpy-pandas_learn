import numpy
import numpy as np

a = np.array([1, 2, 33], dtype=np.float32)
print(a)
print(a.dtype)

b = np.array([[1, 2, 3],
              [4, 5, 6]], dtype=np.float64)

print(b)
print(b.dtype)

c = np.zeros((3, 4), dtype=np.int16)
print('zeros(3,4):', c)

print(c.dtype)

d = np.ones((2, 3, 4), dtype=np.int8)
print('ones(2,3,4):', d)
print(d.dtype)

e = np.empty((3, 4), dtype=np.float64)
print('empty(3,4):', e)
print(e.dtype)

f = np.arange(10, 20, 2, dtype=np.int32)
print('arrage(10,20,2):', f)
print(f.dtype)

g = np.linspace(1, 10, 6, dtype=np.float64)
print('linspace(1,10,6):', g)
print(g.dtype)

h = np.arange(12).reshape(3, 4)
print(h)