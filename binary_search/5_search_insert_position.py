# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# search insert positon

def searchInsertBinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while(left <= right):
        mid = left + (right - left)//2
        
        if(arr[mid] == target):
            return mid
        
        elif(arr[mid] > target):
            right = mid - 1
        
        elif(arr[mid] < target):
            left = mid + 1
    
    return left
    
def searchInsertBinarySearchWithLowerBound(arr, target):
    n = len(arr)
    res = n
    
    left = 0
    right = n - 1
    
    while(left <= right):
        mid = left + (right - left)//2
        
        if(arr[mid] < target):
            left = mid + 1
        
        elif(arr[mid] > target):
            right = mid - 1
            res = mid
        
        elif(arr[mid] == target):
            right = mid - 1
            res = mid
    
    return res

arr = [1, 2, 4, 7]

print("Search insert position solution:", searchInsertBinarySearch(arr, 6))

arr2 = [1,3,5,6]

print("Search insert position solution:", searchInsertBinarySearch(arr2, 5))
print("Search insert position solution:", searchInsertBinarySearch(arr2, 2))
print("Search insert position solution:", searchInsertBinarySearch(arr2, 7))

arr = [1, 2, 4, 7]

print("Search insert position with lower bound solution:", searchInsertBinarySearchWithLowerBound(arr, 6))

arr2 = [1,3,5,6]

print("Search insert position with lower bound solution:", searchInsertBinarySearchWithLowerBound(arr2, 5))
print("Search insert position with lower bound solution:", searchInsertBinarySearchWithLowerBound(arr2, 2))
print("Search insert position with lower bound solution:", searchInsertBinarySearchWithLowerBound(arr2, 7))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------