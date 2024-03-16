import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

dates = pd.date_range('20130101', periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print(df)

df1 = pd.DataFrame(np.random.randn(6,4))
print(df1)

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series([11,22,33,44],index=list(range(2,6)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32')})

print(df2)
print(df2.dtypes)
print('-++++++++++++')
print(df2.columns)
print(df2.values)
print('-++++++++++')
print(df2.describe())
print('-++++++++++')
print(df2.T)
print(df2.T.shape)
print('-++++++++++')
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
print('-++++++++++')
print(df2.sort_values(by='C',ascending=False))