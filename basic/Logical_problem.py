'''' write a program to take 3 sticks and tell wheater that form triangle or not
'''
def triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("yes")
    else:
        print("no")

a,b,c= map(int,input("Enter Side of Triangle\n").split())
triangle(a,b,c)