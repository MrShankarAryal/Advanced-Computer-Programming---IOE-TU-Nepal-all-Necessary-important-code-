class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Name={self.name}\nAge={self.age}"
obj1=student('hari',20)
obj2=student('ram',30)
print(obj1.display())
print(obj2.display())
"""del obj1.name
print(id(obj2.name))
print(id(obj1.name))"""

