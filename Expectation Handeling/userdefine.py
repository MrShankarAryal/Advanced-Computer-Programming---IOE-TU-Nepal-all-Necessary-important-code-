class MyError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
def divide(a,b):
    if b==0:
        raise MyError("Zero division Error")
    else:
        return a/b
try:
    c=divide(1,0)
except MyError as e:
    print(f"Error: {e}")