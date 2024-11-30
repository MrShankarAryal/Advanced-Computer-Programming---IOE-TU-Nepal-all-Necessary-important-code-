import numpy as np


num7=np.random.randint(1,10,size=None)
print(num7)

num7=np.random.randint(1,10,size=10)
print(num7)

num=np.random.randint(1,11,size=(1,))
print(num)

num4=np.random.randint(1,10,size=(2,2))
print(num4)


print("-"*15+"random float in range of [0,1)"+"-"*15)


num1=np.random.rand(1,)

print(num1)

num5=np.random.rand(2,2)
print(num5)

print("-"*15+"random float in range of [A,B-1,size='z']"+"-"*15)




num2=np.random.uniform(1,5,size=None)
print(num2)

num12=np.random.uniform(1,5,size=5)
print(num12)

num6=np.random.uniform(1,11,size=(2,2))
print(num6)

 