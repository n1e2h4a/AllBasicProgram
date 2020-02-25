import numpy as np
import os
sample= np.arange(12).reshape(4, 3)
print("Original array:")
print(sample)
header = 'col1 col2 col3'
np.savetxt('mytext.txt',sample, fmt="%d", header=header)
print("After loading, content of the text file:")
result = np.loadtxt('mytext.txt')
print(result)
