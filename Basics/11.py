## question-11
##this is the bitflip question
##here the printing is done in 0s and 1s
for i in range(5+1): ##the rows remains the same
    if i%2 ==0:
        bits=0
    else:
        bits=1
    for j in range(i):
        print(bits, end= " ")
        bits=1-bits
    print("\n")