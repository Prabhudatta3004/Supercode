##Question-19
## I want to print the pattern
inis=0
for i in range(2*5):
    if i<=5:
        for j in range(5-i):
            print("*",end=" ")
        for j in range(2*i):
            print(" ",end=" ")
        for j in range(5-i):
            print("*",end=" ")
    print("\n")
        
    
