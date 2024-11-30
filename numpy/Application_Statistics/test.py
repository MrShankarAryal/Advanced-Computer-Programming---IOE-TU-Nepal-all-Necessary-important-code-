import numpy as np
a=[1,2,3,5,5,6,7]
mean=np.mean(a)
median=np.median(a)
std=np.std(a)
var=np.var(a)
print(mean)
print(median)
print(std)
print(var)
b=[2,8,9,7,2,1,2]
c=[6,8,2,7,1,1,2]
corrcoef=np.corrcoef(b,c)
cov=np.cov(a,b)
print(corrcoef)
print(cov)