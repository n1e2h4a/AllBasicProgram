import numpy as np
sample = np.ones((3,3))
print("Checkerboard pattern:")
sample = np.zeros((8,8),dtype=int)
sample[1::2,::2] = 1
sample[::2,1::2] = 1
print(sample)

