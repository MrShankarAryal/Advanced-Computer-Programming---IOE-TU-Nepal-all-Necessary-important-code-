"""
ageration is has a relationship n which one class(whole) to reference to other instance of one or more class(parts),but the parts exists independently of whole
"""
class student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
class teacher():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
class classroom():
    def __init__(self,classname,student,teacher):
        self.classname=classname
        self.teacher=teacher
        self.student=student
    def __str__(self):
        return f"{self.student}is with teacher {self.teacher} in class {self.classname}"
s1=student('hari')
t1=teacher('mukesh')
c1=classroom('sh101',s1,t1)
print(c1)