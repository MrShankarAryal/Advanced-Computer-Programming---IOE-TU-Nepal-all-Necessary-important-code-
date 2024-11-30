class opera:
    def __init__(self,width,height):
        self.width=width
        self.height=height
       
    def area(self):
        return self.width*self.height
    def __eq__(self,other):
        return self.area()==other.area()
    def __repr__(self):
        return "opera({self.height},{self.width})"
obj1=opera(1,2)
obj2=opera(2,4)
print(obj1.area())
print(obj2.area())
print(obj1==obj2)