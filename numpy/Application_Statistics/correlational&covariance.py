import numpy as np
#Pearson correlation coefficient matrix
c=np.array([1,2,3,4,5])
d=np.array([6,7,8,9,1])
coorelation_coefficient=np.corrcoef(c,d)
print(coorelation_coefficient)
#Computes the covariance matrix
covariance_matrix = np.cov(c,d)
print(covariance_matrix)