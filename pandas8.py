import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))

data = data.cumsum()

# data.plot()
# 添加标题和标签
# plt.title('Cumulative Sum')
# plt.xlabel('Index')
# plt.show()


df = pd.DataFrame(np.random.randn(4000).reshape(1000, 4),
                  index=np.arange(1000),
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
print(df)
ax = df.plot.scatter(x='A',y='B',color='DarkGreen',label='Class1')
df.plot.scatter(x='A',y='C',color='LightBlue',label='Class2',ax=ax)

plt.show()