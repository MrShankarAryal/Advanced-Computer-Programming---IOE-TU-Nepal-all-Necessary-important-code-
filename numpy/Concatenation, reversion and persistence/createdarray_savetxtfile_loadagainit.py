import numpy as np
a=np.array([[1,2],[3,4]])
np.savetxt("a.txt",a)
load_array=np.loadtxt("a.txt")
print(load_array)