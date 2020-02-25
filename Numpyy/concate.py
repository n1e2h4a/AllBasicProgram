import numpy as np
sample1 = np.array([[0, 1, 3], [5, 7, 9]])
sample2= np.array([[0, 2, 4], [6, 8, 10]])
sample3= np.concatenate((sample1, sample2), 1)
print(sample3)
