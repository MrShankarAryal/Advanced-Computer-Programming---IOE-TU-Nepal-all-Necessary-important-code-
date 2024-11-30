n=eval(input("Enter: "))
a=1
b=1
print(a)
print(b)
c=0
for i in range(1,n-2+1,+1):
    c=a+b
    print(c)
    a=b
    b=c
