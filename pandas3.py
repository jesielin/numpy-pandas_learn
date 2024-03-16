import pandas as pd
import numpy as np

#增  改
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])

print(df)
df.iloc[2,2] = 1111
print(df)
df.loc['20190106','D'] = 2222
print(df)


print(df[df.A>12])
print(df[df>12])    

df['F'] = np.nan
print(df)
df['E'] = pd.Series(np.random.randn(6),index=df.index)
print(df)