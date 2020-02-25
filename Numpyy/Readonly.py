import numpy as np
sample = np.zeros(10)
sample.flags.writeable = False
print("want to Test the array is read-only or not:")
print("lets try to change the value of the first element:")
x[0] = 1