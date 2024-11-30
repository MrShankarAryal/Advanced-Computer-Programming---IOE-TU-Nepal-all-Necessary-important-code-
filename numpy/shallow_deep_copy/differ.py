import numpy as np
a=np.array([1,2,3])
shallow_copy=a.view()
deep_copy=a.copy()

shallow_copy[0]=10
deep_copy[1]=20

print("Original:", a)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)