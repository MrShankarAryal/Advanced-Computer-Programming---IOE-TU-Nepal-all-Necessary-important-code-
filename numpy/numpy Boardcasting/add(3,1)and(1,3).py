import numpy as np
a=np.array([[1,2,3]])
print(np.shape(a))
b=a.reshape(3,1)
print(a)
print(b)
c=a+b
print(c)