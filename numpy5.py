import numpy as np
import torch

a = np.arange(3, 15).reshape(3, 4)

print(a)
print(a[2])

print(a[1][1])
print(a[1, 1])
print(a[2, :])  # 2行全部
print(a[:, 1])  # 1列全部
print(a[1, 1:])  # 1行2到4列

for row in a:
    print(row)

for col in a.T:
    print(col)
print(a.flat)  # 把多维数组降维成一维
print(a.flatten())  # 把多维数组降维成一维
for item in a.flat:
    print(item)

em = torch.arange(24).view(2, 3, 4)
print(em)

print(em.transpose(0, 1))

em = np.array([2.7654, -1.4990, 3.1203, 3.1301, 3.5161, -1.4875, -0.8814, 3.6870,
               3.1434, -1.1957, -1.0852, -1.0249, 2.9040, -1.0137, 3.0623, 2.4806])

score = np.array([-0.0588, -0.0940, -0.0588, -0.0588, -0.0588, -0.0940, -0.0874, -0.0588,
                  -0.0588, -0.0699, -0.0699, -0.0699, -0.0588, -0.0874, -0.0588, -0.0588])
print(em - score)
[8, 2, 8, 8, 8, 2, 0, 8, 8, 1, 1, 1, 8, 0, 8, 8]
result = np.array([[-0.8590, -0.9980, -1.2172, -1.4295, -0.6914, -0.8769, -0.9837, -1.0651, 2.8242],
                   [-0.9951, -1.1727, -1.4049, -1.6536, -0.7516, -1.0384, -1.1602, -1.3634, 3.3663],
                   [-0.9038, -1.1324, -1.3217, -1.6119, -0.6891, -0.9684, -1.0886, -1.2761, 3.1791],
                   [-0.9410, -1.1217, -1.3483, -1.5938, -0.7175, -0.9533, -1.1186, -1.2694, 3.1889],
                   [-1.0543, -1.2705, -1.4877, -1.7782, -0.8126, -1.1310, -1.2520, -1.3618, 3.5749],
                   [-1.0017, -1.1484, -1.3935, -1.6412, -0.7587, -1.0471, -1.1491, -1.3195, 3.3031],
                   [-0.7940, -0.9483, -1.1121, -1.3639, -0.6629, -0.8500, -0.9333, -1.0432, 2.6930],
                   [-1.1087, -1.3041, -1.5672, -1.8341, -0.8522, -1.1483, -1.2801, -1.4098, 3.7458],
                   [-0.9523, -1.1542, -1.3456, -1.6039, -0.7459, -1.0141, -1.1421, -1.2353, 3.2022],
                   [-0.8824, -1.1258, -1.3701, -1.6458, -0.7098, -0.9556, -1.1576, -1.2747, 3.2528],
                   [-0.8545, -1.0153, -1.1977, -1.4212, -0.6609, -0.8560, -0.9465, -1.1510, 2.8544],
                   [-0.8070, -0.9550, -1.1654, -1.3898, -0.6134, -0.7378, -0.9457, -1.1315, 2.6820],
                   [-0.8902, -1.0700, -1.2587, -1.5215, -0.6967, -0.9408, -0.9973, -1.1522, 2.9628],
                   [-0.9263, -1.0888, -1.2960, -1.5460, -0.7052, -0.9815, -1.1006, -1.2752, 3.1382],
                   [-0.9089, -1.0866, -1.3022, -1.5444, -0.7332, -0.9221, -1.0939, -1.2318, 3.1211],
                   [-0.7302, -0.9080, -1.0556, -1.3178, -0.5914, -0.7788, -0.8936, -1.0523, 2.5395]])

# print(em.shape)
# print(em[16,[8, 8, 8, 8, 8, 0, 8, 2, 8, 8, 8, 8, 8, 8, 8, 8]])
