import numpy as np
sample1 = np.array([0,10,20,40,60])
print("first array: ", sample1)
sample2=[10,30,40]
print("first array: ", sample1)
print("similar value between in both arrays:--")
print(np.intersect1d(sample1,sample2))