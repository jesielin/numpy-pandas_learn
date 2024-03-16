import numpy as np

# 拼接

A = np.array([1,1,1,1])
B = np.array([2,2,2,2])

C = np.vstack((A,B))
print(C)

E = np.hstack((A,B))
print(E)

A = A[:,np.newaxis]
B = B[:,np.newaxis]
H = np.concatenate((A,B,A,B),axis=0)
H1 = np.concatenate((A,B,A,B),axis=1)
print('axis 0:',H)
print('axis 1:',H1)

print(A.reshape(4,1))