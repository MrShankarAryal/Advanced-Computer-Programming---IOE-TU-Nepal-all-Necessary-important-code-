class student():
    no_of_student=0 # class or static variable
    def __init__(self):
        self.name=input("name: ") #instance variable name
        self.roll=input("roll: ")
        student.no_of_student=student.no_of_student+1
    def __str__(self):
        return f"Name:{self.name}\nAge:{self.roll}"
obj1=student()
obj2=student()
print(obj1)
print(obj2)
print(student.no_of_student)