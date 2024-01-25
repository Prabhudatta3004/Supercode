'''You are given a sorted integer array 'arr' of size 'n'.

You need to remove the duplicates from the array such that each element appears only once.

Return the length of this new array.'''

##brute force
##convert the array to set
##return the size of the set
##TC=O(nlgn+n)

##Optimized solution
##use two pointers
##remember that the array is sorted
##TC=O(n) SC=O(1)
arr=[1,2,3,3,3,3,4,4,4]
i=0
for j in range(1,len(arr)):
    if arr[j] !=arr[i]:
        arr[i+1]=arr[j]
        i+=1
print(i+1)