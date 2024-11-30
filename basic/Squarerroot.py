import cmath
a=eval(input("Enter coeff of a: "))
b=eval(input("Enter coeff of b: "))
c=eval(input("Enter coeff of c: "))
y=(b**2)-(4*a*c)
x1=(-b+cmath.sqrt(y))/(2*a)
x2=(-b-cmath.sqrt(y))/(2*a)
print(f"Roots:{x1} and {x2}")
