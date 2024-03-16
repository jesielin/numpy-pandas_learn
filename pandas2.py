import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])

print(df)
print(df['A']) #选择列
print(df.A) #选择列
print(df['20190101':'20190103']) #选择行

#按标签选择
print(df.loc['20190101'])
print(df.loc[:,'B'])

#按位置选择
print('-+++++++++')
print(df.iloc[0,1])
print('-+++++++++')
print(df.iloc[0,:])
print('-+++++++++')
print(df.iloc[:,0])
print('-+++++++++')
print(df.iloc[:,0:3])

#boolean indexing
print('-+++++++++')
print(df[df.A>=8])