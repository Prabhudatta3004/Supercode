##question-13
##here we are incrementing the j value after incrementing by 1
##the rows value remains the same as the input
count=1
for i in range(5):
    
    for j in range(i+1):
        print(count, end=" ")
        count +=1
    print("\n")