try:
    file = open("ac.txt","r")
except FileNotFoundError as e:
    print(f"Error:{e}")
else:
    content=file.read()
    print(content)
finally:
    print("sucefully")
    if 'file' in locals():
           file.close()
