def hcf(a,b):
    if a>b:
        s=b
    else:
        s=a
    for i in range(1,s+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
a=eval(input("enter"))
b=eval(input("enter"))
print(hcf(a,b))

