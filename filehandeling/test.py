with open("test.bin","wb") as file:
    n=int(input("Enter no.of student: "))
    for i in range(n):
        print("Enter student no: {i+1} info ")
        sname=input("enter name: ")
        sage=int(input("enter age: "))
        forma=f"Name={sname}\nAge={sage}\n"
        file.write(forma.encode())
with open("test.bin","rb") as file:
    content=file.read()
    print(content.decode())
