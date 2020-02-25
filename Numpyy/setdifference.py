import numpy as np
sample1 =np.array([0,10,20,40,60])
print("Array first: ",sample1)
sample2 =[10,30,40,50,70]
print('array second: ',sample2)
print("uniq value in sample1 that are not in sample2")
print(np.setdiff1d(sample1,sample2))