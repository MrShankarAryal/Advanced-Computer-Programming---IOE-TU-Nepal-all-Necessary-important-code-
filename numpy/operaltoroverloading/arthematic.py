class opera:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return opera(self.x+other.x,self.y+other.y)
    def __truediv__(self,other):
        return opera(self.x/other.x,self.y/other.y)
    def __repr__(self):
        return f"{self.x} ,{self.y}"
print("object1 enter: ")
obj1=opera(4,2)
print("object2 enter: ")
obj2=opera(2,2)
print(obj1+obj2)
print(obj1 / obj2)