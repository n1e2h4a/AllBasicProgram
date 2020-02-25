import numpy as np
sample=np.array([1.6e-10, 1.6, 1200, .235])
print("Real array elements:")
print(sample)
print("Print array values with precision 3:")
np.set_printoptions(suppress=True)
print(sample)