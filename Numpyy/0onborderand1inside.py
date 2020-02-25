import numpy as np
reshape=np.ones((3,3))
print("the original sample is:-")
print(reshape)
print("border with zero and 1 inside")
reshape = np.pad(reshape,pad_width=1,mode="constant",constant_values=0)
print(reshape)