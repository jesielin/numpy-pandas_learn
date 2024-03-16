import numpy as np

#分割

A = np.arange(12).reshape(3,4)
print(A)

print(np.split(A,4,-1)) #均分

print(np.array_split(A,3,axis=1)) #非均分

print(np.vsplit(A,3))
print(np.hsplit(A,4))