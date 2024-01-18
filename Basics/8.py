##pattern-8
##it is just the inverted pyramid
##we will follow the same procedure of space, star, space
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