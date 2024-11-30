"""""
 Built-in functions are functions that are already de ned in the Python interpreter. They can be used to perform common tasks such as printing
 to the console, converting between data types, or working with strings and lists.
 print(): Outputs text or variables to the console.
 input(): Reads user input from the console.
 len(): Returns the length of an object (e.g., string, list, tuple).
 range(): Generates a sequence of numbers, often used in loops.
 type(): Returns the type of an object.
 int(), oat(), str(): Convert values between different data types.
 max() and min(): Return the maximum and minimum values in a sequence.
 sum(): Calculates the sum of all items in an iterable.
 sorted(): Returns a new sorted list from an iterable.
 abs(): Returns the absolute value of a number.
 round(): Rounds a number to a speci ed number of decimal places.
 open(): Opens a le and returns a le object.
 dir(): Returns a list of valid attributes and methods of an object.
 help(): Provides help documentation for an object.
 enumerate(): Returns an enumerate object, often used to get index and value pairs from a sequence.
 And many more...
"""""
num = [5, 2, 8, 1, 9, 3, 7] 
print("Original list:", num)
list_length = len(num)
print("Length of the list:", list_length)
sorted_num = sorted(num)
print("Sorted list:", sorted_num)
print("\nIndex and value pairs:")
for i in range(len(num)):
    print(f"Index {i}: {num[i]}")