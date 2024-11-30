class student:
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
    def display(self):
        return f"Name={self.name}\nAge={self.age}"
obj1=student()
obj2=student()
print(obj1.display())
print(obj2.display())
del obj1.name
print(id(obj2.name))
print(id(obj1.name))

