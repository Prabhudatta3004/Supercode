
##pattern-9
##we are printing a prism
##just the addition of the above code
for i in range(5): # no of rows
    ##for spaces
    for j in range(0,5-i-1):
        print(" ", end=" ")
    ##for stars
    for j in range(0,2*i+1):
        print("*", end=" ")
    ##for spaces
    for j in range(0,5-i-1):
        print(" ", end=" ")
    print("\n")
for i in range(5): # no of rows
    ##for spaces
    for j in range(0,i):
        print(" ", end=" ")
    ##for stars
    for j in range(0,2*(5-i)-1):
        print("*", end=" ")
    ##for spaces
    for j in range(0,i):
        print(" ", end=" ")
    print("\n")