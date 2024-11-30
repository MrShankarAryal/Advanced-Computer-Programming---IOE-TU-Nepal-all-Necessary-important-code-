try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Enter an index to access: "))
    a=my_list[index]
except IndexError:
    print("Error: Index out of range.")
else:
    print(a)
finally:
    print("sucesful")