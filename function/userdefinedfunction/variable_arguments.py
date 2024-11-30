def elementsum(*list):
    c=0
    for items in list:
        c=c+items
    return c
list=eval(input("Enter in formated [1,2,3] : "))
print(elementsum(*list))