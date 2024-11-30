'''
3x+4y=10
2x-y=3
'''
import numpy as np
a=np.array([[3,4],[2,-1]])
b=np.array([10,3])
output=np.linalg.solve(a,b)
print(output)