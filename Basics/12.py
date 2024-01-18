##question-12
##for printing this, we used the same thing space, stars, space
##the spaces seems to be in the order 2*(n-i)-2
##the values on both sides seems to be the value of j

for i in range(1,5):
    ##for values
    for j in range(1,i):
        print(j,end=" ")
    
    ##for spaces
    for j in range(2*(4-2)-2):
        print(" ", end=" ")

    ##for values
    for j in range(1,5):
        print(j,end=" ")
    print("\n")
        