# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Floor value

def floorBinarySearch(arr, target):
    n = len(arr)
    res = arr[0]
    
    left = 0
    right = n - 1
    
    while(left <= right):
        mid = left + (right - left)//2
        
        if(arr[mid] == target):
            res = arr[mid]
            return res
        
        elif(arr[mid] < target):
            res = arr[mid]
            left = mid + 1
        
        elif(arr[mid] > target):
            right = mid - 1
    
    return res
    
arr = [10, 20, 30, 40, 50]
print("Floor value for 25 is:", floorBinarySearch(arr, 25))
print("Floor value for 35 is:", floorBinarySearch(arr, 35))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------