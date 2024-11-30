class student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
obj1=student()
name=input('enter name')
obj1.setName(name)
print(obj1.getName())