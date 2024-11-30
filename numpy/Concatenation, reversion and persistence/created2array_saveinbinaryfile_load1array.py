import numpy as np
a=np.array([[1,2],[2,3]])
b=np.array([[4,5],[4,4]])
np.savez("ab.npz",c=a,d=b)
load_ad=np.load("ab.npz")
print(load_ad['c'])
print(load_ad['d'])