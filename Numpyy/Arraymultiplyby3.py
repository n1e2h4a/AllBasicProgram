import numpy as np
sample= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(sample)
for a in np.nditer(sample, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(sample)