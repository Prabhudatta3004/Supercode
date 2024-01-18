##Question-17
##this is a pattern where we use the logic of symmetry
##symmetry occurs at the center
## it is basically the ceil of the half of the no
##the no of rows remains the same
##the spaces are in the form (n-i-1)
##total characters to be printed are 2(i)+1
from math import ceil

for i in range(4):
    # For spaces before characters
    for j in range(0, 4 - i - 1):
        print(" ", end=" ")

    # For characters
    ch = ord("A")
    mid = ceil((2 * i + 1) / 2)
    for j in range(0, 2 * i + 1):
        print(chr(ch), end=" ")
        if j < mid - 1:
            ch += 1
        else:
            ch -= 1

    # For spaces after characters
    for j in range(0, 4 - i - 1):
        print(" ", end=" ")

    print("\n")