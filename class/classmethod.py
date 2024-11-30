class myclass:
    no_of_student=0
    def __init__(self):
        self.name=input("Enter ")
        myclass.no_of_student += 1
    @classmethod
    def counting(cls):
        print(f"No of instance: {cls.no_of_student} ")
obj1=myclass()
obj2=myclass()
obj3=myclass()
myclass.counting()