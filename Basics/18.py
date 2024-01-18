##Question-18
##the pattern seems to be a right angled triangle
##here the printing value changes
##the skeleton remains the same
for i in range(5):
    for j in range(i+1):
        print("_",end=" ")
    print("\n")

for i in range(5):
    ch=ord("A")+5-i-1
    for j in range(i+1):
        print(chr(ch), end=" ")
        ch+=1
    print("\n")