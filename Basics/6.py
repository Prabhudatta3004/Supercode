##pattern-6
##it is just like the above one, but here we are printing the values of j starting from 1

for i in range(5):
    for j in range(1, 5-i+1):
        print(j, end=' ')
    print("\n")