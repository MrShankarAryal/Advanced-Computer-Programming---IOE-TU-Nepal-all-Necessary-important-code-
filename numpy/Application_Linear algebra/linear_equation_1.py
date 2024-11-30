'''
2x+y = 1
x+3y = 2

'''
import numpy as np
a=np.array(
          [[2,1],
           [1,3]]
           )
b=np.array(
    [1,2]
)
output=np.linalg.solve(a,b)
print(output)