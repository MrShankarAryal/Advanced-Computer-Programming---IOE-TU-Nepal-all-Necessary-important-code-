
a=eval(input("Enter angle "))
n=eval(input("Enter itteration"))
r=((22/7)*a)/180
t=1
sum=1
print(sum)
i=1
for j in range(2,n+1):
    t=(-1)*t*r*r/(i*(i+1))
    sum=sum+t
    print(sum)
    i=i+2