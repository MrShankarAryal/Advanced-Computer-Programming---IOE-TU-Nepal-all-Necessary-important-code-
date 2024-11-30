import numpy as np
a=np.array([4,1,2,3])
a.sort()
print(a)

b=np.array([4,10,3,9])
c=np.sort(b,axis=0)
d=np.sort(b,axis=-1)

print(c,"accending")
print(d,"decending")

'''
np.sort(): Sorts the array without changing the original array. It returns a sorted copy.
arr.sort(): Modifies the original array in place, instead of creating a sorted copy.
'''