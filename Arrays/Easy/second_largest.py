'''You have been given an array ‘a’ of ‘n’ unique non-negative integers.

Find the second largest and second smallest element from the array.

Return the two elements (second largest and second smallest) as another array of size 2.
'''

##Brute force
##my idea says that i can sort the given array and return the 2nd element and the n-2 element
arr=[1,2,4,11,42,11,51]
arr.sort()
print(arr[1],arr[len(arr)-2])

##the time complexity will be O(nlgn) since it uses timsort 
## also for an array where the max occurs more than once lets say when we sort
## array becomes [1,2,3,4,5,6,6] ##instead of returning 5 it will return 6

##Better solution
##Pass the array twice once for largest/smallest 
##next for second largest or second smallest

arr=[1,2,53,21,56,56,24,11]
largest= arr[0]
##first pass
for i in range(1,len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

##second pass 
second=-1
for i in range(len(arr)):
    if arr[i]>second and arr[i]!= largest:
        second=arr[i]
print(second)

##similarly for second smallest 
##first pass
smallest= arr[0]
for i in range(len(arr)):
    if arr[i]< smallest:
        smallest=arr[i]
print(smallest)

##second pass
second_smallest= 102323141
for i in range(len(arr)):
    if arr[i]< second_smallest and arr[i]!=smallest:
        second_smallest=arr[i]
print(second_smallest)

## this approach takes time O(N+N)

## optimized solution
## we will take a single pass
## will relay the values when we change it
##compare once, update both

largest=arr[0]
second_largest=-1
for i in range(len(arr)):
    if arr[i]> largest:
        second_largest=largest
        largest=arr[i]
    if arr[i]< largest and arr[i]>second_largest:
        second_largest=arr[i]
print(largest,second_largest)

##same goes for the smallest
smallest=arr[0]
second_smallest=121423131
for i in range(len(arr)):
    if arr[i]<smallest:
        second_smallest=smallest
        smallest=arr[i]
    if arr[i]>smallest and arr[i]<second_smallest:
        second_smallest=arr[i]
print(smallest, second_smallest)

##Time taken will be O(n)

