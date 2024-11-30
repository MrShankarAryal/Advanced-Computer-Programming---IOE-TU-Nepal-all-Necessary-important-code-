n=10
for i in range(1,n+1,+1):
    if i ==5:
        continue # it will skip the current itteration and move to next
    print(i)  
print("\n")
m=0
for j in range(10,m-1,-1):
    if j==5:
        break #it will terminated the loop as it is encountered
    print(j)