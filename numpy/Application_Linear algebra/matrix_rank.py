'''
1 2 3 
4 5 6 

'''
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
rank=np.linalg.matrix_rank(a)
print(rank)