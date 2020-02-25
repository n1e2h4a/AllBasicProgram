import numpy as np
sample = np.ones((5,5))
print("Real array:")
print(sample)
print("1 on the border and 0 inside in the array")
sample[1:-1,1:-1] = 0
print(sample)
