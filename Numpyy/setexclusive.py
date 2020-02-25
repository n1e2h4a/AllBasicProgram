import numpy as np
sample1 = np.array([0, 10, 20, 40, 60, 80])
print("sample1: ",sample1)
sample2 = [10, 30, 40, 50, 70]
print("sample2: ",sample2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(sample1, sample2))
