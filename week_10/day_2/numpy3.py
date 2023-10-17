# importing dependencies 
import pandas as pd 
import numpy as np 

# creating a series by passing a list of valuess, letting pandas create a default rangeindex
n = pd.Series([1,3,5,np.nan,6,0])
# print (n)

dates = pd.date_range("20230101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df.head()
df.index
df.columns
df.to_numpy()
df.describe()
df.dtypes
df.T
df.sort_index(axis=1,ascending=False)
df.sort_index(axis=0, ascending=False)
df.sort_values(by='B')




