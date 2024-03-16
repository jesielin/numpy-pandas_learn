import pandas as pd
import numpy as np

data = pd.read_csv('student.csv')
print(data)
print(type(data))

data.to_excel('student.xlsx')
