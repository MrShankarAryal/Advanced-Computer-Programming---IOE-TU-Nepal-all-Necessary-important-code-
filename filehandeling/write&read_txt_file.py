# Writing to a binary file
file = open("student.bin", "wb")
n = int(input("Enter the number of students: "))
for i in range(n):
    print(f"Info for student {i+1}")
    sid = input("Enter ID: ")
    sname = input("Enter name: ")
    sage = int(input("Enter age: "))
    saddress = input("Enter address: ")
    
    # Format the student info as a string
    student_info = f"ID: {sid}\nName: {sname}\nAge: {sage}\nAddress: {saddress}\n\n"
    
    # Convert the string to bytes and write to the binary file
    file.write(student_info.encode())
file.close()

# Reading from the binary file
file = open("student.bin", "rb")
content = file.read()

# Convert bytes back to string and print
print(content.decode())
file.close()
