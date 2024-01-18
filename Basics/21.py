##Question-21
##we are printing a box
##only the borders have stars and otherwise spaces
for i in range(4):
    for j in range(4):
        if(i==0 or i==4-1 or j==0 or j==4-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")