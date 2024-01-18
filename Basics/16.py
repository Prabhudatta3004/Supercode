##Question-16
##this is a right angled pyramid but here the pattern prints chr(ord("A")+i) 

for i in range(5):
    for j in range(i+1):
        print(chr(ord("A")+i), end=" ")
    print("\n")