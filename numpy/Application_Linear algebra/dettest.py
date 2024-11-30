import numpy as np
a=np.array([[1,2,3],[2,2,2],[3,0,5]])
b=np.linalg.eig(a)
print(b)