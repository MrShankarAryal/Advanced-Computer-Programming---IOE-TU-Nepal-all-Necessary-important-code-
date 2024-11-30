import numpy as np
# Indexing a 1D array
array = np.array([10, 20, 30, 40, 50])
print(array[0]) # Output: 10
print(array[2]) # Output: 30
# Slicing a 1D array
slice_array = array[0:4]
print(slice_array) # Output: [10 20 30 40]
# Indexing a 2D array
array_2d = np.array([[1, 2, 3,4,5],[1, 2, 3,4,5],[1, 2, 3,4,5],[1, 2, 3,4,5]])
print(array_2d[0, 1]) # Output: 20
# Slicing a 2D array
sub_matrix = array_2d[1:4, 1:4]
print(sub_matrix)
sub2=array_2d[1:4,0:3]
print(sub2)


