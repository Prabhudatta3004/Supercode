##pattern-5
## it is a printing in reverse order. ## it at first prints the n no of stars then reduces the stars as we go down
##looks like an inverted right angled triangle

for i in range(5):
    for j in range(0,5-i):
        print("*", end =" ")
    print("\n")
        