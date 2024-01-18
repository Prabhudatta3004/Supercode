##question-20
##here at first we need to print the upper half
for i in range(10-1):
    if i <= ceil(10-1/2):
        for j in range(i+1):
            print("*", end=" ")
        for j in range(