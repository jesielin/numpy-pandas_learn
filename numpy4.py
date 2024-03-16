
import numpy as np

a = np.arange(2,14).reshape((3,4))
print(a)

print(np.argmax(a))
print(np.argmin(a))
print(np.mean(a))
print(np.average(a))
print(np.median(a)) #中位数
print(np.cumsum(a)) #累加
print(np.diff(a)) #累减
print(np.nonzero(a))#非零位置
print(np.sort(a))#排序
print(np.transpose(a))#转置
print(a.T)#转置
print(np.clip(a,5,9))#裁剪
print(np.mean(a,axis=0))#按列求均值