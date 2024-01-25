'''You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.

Your task is to return 1 if the given array is sorted. Else, return 0.
'''

## i have an approach that will take O(n)
##lets say we can have one pass through the array
##now when we pass through the array if any value is less than its previous value
## we can return false


arr=[1,2,3,4,5,6,7,3]
previous= arr[0]
for i in range(1, len(arr)):
    if arr[i]< previous:
        print(False)
    previous=arr[i]
print(True)