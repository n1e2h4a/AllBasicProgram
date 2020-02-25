import numpy as np
sample = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 4, 6]
print("Original array:")
print(sample)
print("Delete first, fifth and seventh elements:")
new_sample = np.delete(sample, index)
print(new_sample)