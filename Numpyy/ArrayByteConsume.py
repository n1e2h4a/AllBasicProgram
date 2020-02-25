import numpy as np
sample = np.array([1,2,3], dtype=np.float64)
print("size of the array:", sample.size)
print("length of the each array element in bytes:", sample.itemsize)
print("Total bytes consumed by the elements of the array:", sample.nbytes)