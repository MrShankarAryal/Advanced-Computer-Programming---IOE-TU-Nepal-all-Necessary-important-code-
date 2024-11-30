
class Student:
  def __init__(self):
    self.id=int(input("Enter id : "))
    self.name=str(input("Enter name : "))
    self.address=str(input("Enter address : "))
  def display(self):
    print(f"ID={self.id}\nName={self.name}\nAddress={self.address}")
class Teacher(Student):
  def __init__(self):
    super().__init__()
    self.salary=float(input("Enter Salary : "))
  def display(self):
    super().display()
    print(f"salary={self.salary}")
obj1=Student()
obj2=Teacher()
obj1.display()
obj2.display()