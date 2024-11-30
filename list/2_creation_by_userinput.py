n1 = int(input("Enter the number of integers: "))
int_list1 = []
for _ in range(n1):
        num = int(input("Enter an integer: "))
        int_list1.append(num)
print(int_list1)

# using Map method 
n = int(input("Enter the number of integers: "))
print("Enter the integers separated by space:")
int_list = list(map(int, input().split()[:n]))
print("Your integer list:", int_list)


""" IF you wanted mixed type the just write
num = input("Enter an integer: ")
for another method
int_list = list(map( input().split()[:n]))

"""