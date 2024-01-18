#Question-14
##this is now a character pattern, the no of rows remains the same as the input value
##it is a right angled pyramid where each value is just the value of j 
##we will use a new function called ord() this is new to the author, ord() converts a character into its unicode form
##by using ord we can convert "a" to 97 etc.

for i in range(5):
    for j in range(i+1):
        print(chr(ord("A")+j),end=" ")
    print("\n")