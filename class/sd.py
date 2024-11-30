class engine:
    def __init__(self,hp):
        self.hp=hp
    def __str__(self):
        return f"{self.hp}"
class car:
    def __init__(self,model,hp):
        self.model=model
        self.engine=engine(hp)
    def __str__(self):
        return f"{self.model}has{self.engine}"
mycar=car('toyota',2000)
print(mycar)
