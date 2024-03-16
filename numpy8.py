import numpy as np

#复制

A = np.arange(12).reshape(3,4)
B = A.copy() #deep copy
# B = A[:,:] #等同于B = A

print(B)

A[0][0] = 55

print(A)
print(B)