import numpy as np
a=np.array([[1,2],[2,3]])
np.save("a.npy",a)
load_array=np.load("a.npy")
print(load_array)