# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Finding lower bound
# a lower bound is smallest index such that arr[index] >= n

# in easy words
# find the element (arr[index]) in the array that is >= n, then get its index
# if there are multiple elements with the same value, return the smallest index

arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]

def lowerBound(arr, x):
    n = len(arr)
    res = n
    
    left = 0
    right = n - 1
    
    while(left <= right):
        mid = left + (right - left)//2
        if(arr[mid] < x):
            left = mid + 1
        
        elif(arr[mid] > x):
            right = mid - 1
            res = mid
        
        elif(arr[mid] == x):
            right = mid - 1
            res = mid
    
    return res
    
print("The lower bound for 1 is:", lowerBound(arr, 1))
print("The lower bound for 9 is:", lowerBound(arr, 9))
print("The lower bound for 6 is:", lowerBound(arr, 6))
print("The lower bound for 10 is:", lowerBound(arr, 10))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------