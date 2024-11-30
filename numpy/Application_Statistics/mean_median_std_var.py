import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
#mean
mean=np.mean(a)
print(mean)
#median
median=np.median(a)
print(median)
#standar deviation
standar=np.std(a)
print(standar)
#variance 
variance=np.var(a)
print(variance)
#Pearson correlation coefficient matrix
c=np.array([1,2,3,4,5])
d=np.array([6,7,8,9,1])
coorelation_coefficient=np.corrcoef(c,d)
print(coorelation_coefficient)
#minmum
min=np.min(a)
print(min)
# maximum
max=np.max(a)
print(max)
