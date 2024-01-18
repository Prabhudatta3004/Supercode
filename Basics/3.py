## pattern-3
#to print nos, the first index is 1 then 2 then soo on
##looks like we are printing the j value
for i in range(5+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")