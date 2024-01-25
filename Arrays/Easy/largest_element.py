'''Question: Find the largest element in the arrray'''

##Brute force approach- sort the array and the element in the position -1 is the largest

def brute():
    arr=[1,3,4,2,14,5]
    arr.sort()
    print(arr[-1])
##Time complexity here is O(nlgn) since the used sorting algo is timsort which is a hybrid of
## merge sort and insertion sort


##Better approach can be we can consider the first element to be the largest
## swipe through the list and just update the largest and return the largest

def better():
    arr=[1,3,4,2,14,5]
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>= largest:
            largest=arr[i]
    print (largest)

##Time complexity is better than the previous since here the time is O(n)