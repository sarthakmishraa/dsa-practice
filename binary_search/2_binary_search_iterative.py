# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# iterative binary search

def iterativeBinarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = left + (right - left)//2
        if(arr[mid] == target):
            return True
        
        elif(arr[mid] < target):
            left = mid + 1
        
        elif(arr[mid] > target):
            right = mid - 1
    
    return False

arr = [3, 4, 6, 7, 9, 12, 16, 17]

print("Recursive Binary Search's solution: " + str(iterativeBinarySearch(arr, 12)))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------