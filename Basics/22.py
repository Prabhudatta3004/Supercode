##Question-22
## it is quite complicated to find such a pattern at one go
##it is a box for sure. so we know that the values for i,j will be equal
##now for each value we can see that the n=4 and the size of the box is 2*n-1
## now for the values we can see that the minimum distance of a point when we consider top, down, left and right is being taken
## do a n-value to get the intial values and then revert it to get the original box
for i in range(2*4-1):
    for j in range(2*4-1):
        top=i
        left=j
        bottom=(2*4-2)-i
        right=(2*4-2)-j
        print(4-min(min(top,bottom),min(left,right)),end=" ")
    print("\n")