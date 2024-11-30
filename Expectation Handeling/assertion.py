"""
AssertionError is an error that occurs when an assert statement fails.
The assert statement is used to test if a condition is true. 
If the condition evaluates to False, Python raises an AssertionError. 
It's a debugging aid that tests certain assumptions in the code. 
Assertions are often used to catch and debug code issues early.

"""

"""assert condition, optional_message"""

"It only displays a message or raises an error when the condition is false."

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number b"))
    assert b!=0,"division by zero Error"
    c=a/b
except AssertionError as e:
    print(f"Assertion Error:{e}")
else:
    print(c)
