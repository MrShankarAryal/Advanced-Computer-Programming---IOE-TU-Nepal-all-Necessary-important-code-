import numpy as np
# Indexing a 1D array
array = np.array([10, 20, 30, 40, 50])
print(array[0])#10
print(array[3])#40
array_2d = np.array([[1, 2, 3,4,5],[6,7,8,9,0],[5,4,3,2,1],[0,9,8,7,6]])
print(array_2d[1:3,1:4])
print("-"*30+"\n")
print(array_2d[2:4,0:2])
print("-"*30+"\n")
print(np.size(array_2d))
print(np.shape(array_2d))

b=array_2d.reshape(5,4)
print(b)

