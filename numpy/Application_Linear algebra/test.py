# 3x+4y=10
# 2y-y=3
import numpy as np
a=np.array([[3,4],[2,-1]])
b=np.array([10,3])
c=np.linalg.solve(a,b)
print(c)