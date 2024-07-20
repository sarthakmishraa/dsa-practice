# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Finding upper bound
# an upper bound is a smallest index such that arr[index] > n

# in easy words
# find the element(arr[index]) which is the next greater element than n,
# then return its index

# if there are multiple elements with the same value,
# then return the smallest index of the element which is greater than n

# if there is no element that is bigger than n, then return size of the array

def upperBound(arr, x):
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
            left = mid + 1
    
    return res

arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
print("The upper bound for 6 is:", upperBound(arr, 6))
print("The upper bound for 11 is:", upperBound(arr, 11))
print("The upper bound for 12 is:", upperBound(arr, 12))
print("The upper bound for 13 is:", upperBound(arr, 13))
print("The upper bound for 0 is:", upperBound(arr, 0))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------