class Animal:
    def __init__(self):
        self.type="animal"
        print(f"{self.type}")
        super().__init__()
    
class Bird:
    def __init__(self):
        self.type="bird"
        print(f"{self.type}")
        super().__init__()
    
class sparrow(Animal,Bird):
    def __init__(self):
        self.type="sparrow"
        print(f"{self.type}")
        super().__init__()
    
sp=sparrow()
