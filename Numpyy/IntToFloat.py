import numpy as np
sample = np.array([[2,4,6],[6,8,10]], np.int32)
print(sample)
print('Data typr of the array sample is:',sample.dtype)
sample2 = sample.astype(float)
print("new array in float form",sample2.dtype)
print(sample2)