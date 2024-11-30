try:
    a=int(input("Enter"))
    b=int(input("Entre"))
    c=a/b
except ZeroDivisionError as e:
    print(f"Error:{e}")
except:
    print("Somethong Went rrong")
else:
    print(f"{c}")
finally:
    print("Program Executed....22")