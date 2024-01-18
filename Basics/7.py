##pattern-7 
##to print a pyramid of stars
##always look for spaces, stars, spaces
## patterns are clear, for spaces the pattern is n-i-1
## for stars its 2*i+1

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