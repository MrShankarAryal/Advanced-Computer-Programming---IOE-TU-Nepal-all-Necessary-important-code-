# horizontal concatenated
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[6,7],[8,9]])

"""c=np.concatenate((a,b),axis=1)
print(c)
#or
e=np.hstack((a,b))
print(e)"""

#vartical conactenated
d=np.concatenate((a,b),axis=0)
print(d)
#or
f=np.vstack((a,b))
print(f)
