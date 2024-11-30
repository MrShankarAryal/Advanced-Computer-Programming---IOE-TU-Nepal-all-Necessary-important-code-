class engine:
    def __init__(self,hp):
        self.hp=hp
    def __str__(self):
        return f"{self.hp}"
class car:
    def __init__(self,cname,model,hp):
        self.cname=cname
        self.model=model
        self.engine=engine(hp)
    def __str__(self):
        return f"{self.cname} of {self.model} has {self.engine}"
obj1=car("toato",2020,7000)
print(obj1)
