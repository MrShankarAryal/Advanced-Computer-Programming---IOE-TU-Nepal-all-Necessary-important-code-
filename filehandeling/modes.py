'''with open("std2.txt","w")as file:
    n=int(input("Enter number of student"))
    for i in range(n):
        print(f"Info for student {i+1}")
        sid=input("Enter ID: ")
        sname=input("Enter name: ")
        sage=int(input("Enter age: "))
        saddress=input("Enter address: ")
        file.write(f"ID: {sid}\nName: {sname}\n Age: {sage} \nAddress: {saddress}")


     '''

"""with open("std2.txt","w")as file:
    file.write("w\nto write\nIf data is already present in the file,it would be deleted and present data would be stored")
"""

"""with open("std2.txt","w+")as file:
    file.write("W+\nwrite and read.\nprevious data will be deleted")
    content=file.read()
    print(content)
"""
"""
with open("std2.txt","r")as file:
    content=file.read()
    print(content)
"""

"""""
with open("std2.txt","r+")as file:
    content=file.read()
    print(content)
    file.write("\nr+\n read and write.\n The previous data will not be deleted \n file pointer is at begining\n")

"""""
"""
with open("std2.txt","a")as file:
    file.write("\nTo appened\nAppending means adding the data at the last\nFile pointer is at the end of file\nIf File doesn't exist then it will createdd new to write\n")
"""
with open("std2.txt","a+")as file:
    file.write("\nTo appened and read data of file \nFile pointer is at the end of file \nIf File doesn't exist then it will createdd new for reading and writing\n")
