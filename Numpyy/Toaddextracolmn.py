import numpy as np
samplex = np.array([[10,20,30], [40,50,60]])
sampley = np.array([[100], [200]])
print(np.append(samplex, sampley, axis=1))
