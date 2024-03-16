import pandas as pd
import numpy as np

#concatenating dataframes
df1 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(12,24).reshape(3,4), columns=['a','b','c','d'])
df3 = pd.DataFrame(np.arange(24,36).reshape(3,4), columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print('-+++++++++++++')
print(res)
res = pd.concat([df1,df2,df3],axis=1,ignore_index=True)
print('-+++++++++++++')
print(res)

res = pd.concat([df1,df2,df3])
print('-+++++++++++++')
print(res)

df1 = pd.DataFrame(np.ones(12).reshape(3,4)*0,index=[1,2,3],columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones(12).reshape(3,4)*1,index=[2,3,4],columns=['b','c','d','e'])
print('-+++++++++++++')
print(df1)
print(df2)

res = pd.concat([df1,df2],axis=0,ignore_index=True)
print('-+++++++++++++')
print(res)

res = pd.concat([df1,df2],join='inner',ignore_index=True)
print('-++++++++++++++')
print(res)

res = pd.concat([df1,df2],join='outer',ignore_index=True)
print('-++++++++++++++')
print(res)


res = pd.concat([df1,df2],axis=1,join='outer')
print('-++++++++++++++')
print(res)

res = pd.concat([df1,df2],axis=1)
print('-++++++++++++++')
print(res)

print(df1)
print(df2)
print(df3)

