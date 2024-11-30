with open("ss.txt","w") as file:
    n=int(input("Enter "))
    for i in range(n):
        print(f"for {i+1}\n")
        sname=input("enter ")
        sage=int(input("enter "))
        file.write(f"name={sname}\nage={sage}")
with open("ss.txt","r") as file:
    content=file.read()
    print(content)