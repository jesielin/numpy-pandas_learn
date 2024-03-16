import pandas as pd
import numpy as np

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'A':['A0','C1','A2','C3'],
                      'D':['D0','D1','D2','D3']})

print(left)
print(right)

res = pd.merge(left,right,on='key')
print(res)


res = pd.merge(left,right,on=['A','key'])
print(res)

#how = ['left', 'right', 'outer', 'inner']
res = pd.merge(left,right,on=['A','key'],how='outer',indicator='indicator_column')
print(res)

res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)