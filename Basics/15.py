##Question-15 
##this is just the inverted right angled triangle we just did in the above question
for i in range(5):
    for j in range(5-i):
        print(chr(ord("A")+j),end=" ")
    print("\n")