# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Ceil value

def ceilBinarySearch(arr, target):
    n = len(arr)
    res = arr[n - 1]
    
    left = 0
    right = n - 1
    
    while(left <= right):
        mid = left + (right - left)//2
        
        if(arr[mid] == target):
            res = arr[mid]
            return res
        
        elif(arr[mid] < target):
            left = mid + 1
        
        elif(arr[mid] > target):
            right = mid - 1
            res = arr[mid]
        
    return res

arr = [10, 20, 30, 40, 50]
print("Ceil value for 25 is:", ceilBinarySearch(arr, 25))
print("Ceil value for 35 is:", ceilBinarySearch(arr, 35))
print("Ceil value for 15 is:", ceilBinarySearch(arr, 15))
print("Ceil value for 20 is:", ceilBinarySearch(arr, 20))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------