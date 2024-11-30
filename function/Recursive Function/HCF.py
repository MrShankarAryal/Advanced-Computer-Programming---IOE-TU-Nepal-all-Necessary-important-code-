def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b, a%b)
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print(f"HCF of {first} and {second} is {hcf(first,second)}")