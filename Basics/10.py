##question-10
##this is a symmetry question
##we found that there is a symmetry at the middle line
##we will have two blocks one the upper half and the other as the lower half
from math import *
threshold=ceil((2*5-1)/2)
for i in range(0,2*5-1):
    if i <threshold:
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(1,2*5-i):
            print("*", end =" ")
    print("\n")