# lambda is an anonumus function that doesn't have defined name of function
# lambda function is also called single line function as it is written in one line
square=lambda x: x**x
print(square(2))


greter=lambda a,b: f"a={a} is greater" if a>b else f"b={b} is greater"
print(greter(2,3))

check=lambda a: f"{a} is even"if a%2==0 else f"{a} is odd"
print(check(2))

list1=[1,2,3]
list2=[2,2,2]
list3=list(map(lambda x,y:x*y,list1,list2))
list4=list(map(lambda x,y:x+y,list1,list2))
list5=lambda list1,list2:list1+list2
print(list3)
print(list4)
print(list5(list1,list2))

