class myclass:
    no_of_student=0
    def __init__(self):
        myclass.no_of_student += 1
    @staticmethod
    def counting():
        print(f"No of instance: {myclass.no_of_student} ")
obj1=myclass()
obj2=myclass()
obj3=myclass()
myclass.counting()