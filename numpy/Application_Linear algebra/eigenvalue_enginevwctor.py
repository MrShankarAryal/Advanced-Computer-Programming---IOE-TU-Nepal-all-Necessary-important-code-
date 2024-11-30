import numpy as np
a=np.array([[1,2],
           [3,4]])
value,vector=np.linalg.eig(a)
print(value)
print(vector)