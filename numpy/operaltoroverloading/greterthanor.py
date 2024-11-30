class opera:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __ge__(self,other):
        return self.x>=other.y,self.x>=self.y
    def __repr__(self):
        return f"{self.x,self.y}"
obj1=opera(1,2)
obj2=opera(2,1)
print(obj1>=obj2)