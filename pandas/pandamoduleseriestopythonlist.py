import pandas as pd
sample = pd.Series([9,18,27,36,45])
print("pandas series and type")
print(sample)
print(type(sample))
print('now converted in pandas series to python list')
print(sample.tolist())
print(type(sample.tolist()))

