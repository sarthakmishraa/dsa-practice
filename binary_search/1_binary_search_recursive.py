# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# recursive binary search

def recursiveBinarySearch(arr, target, left, right):
    mid = left + (right - left)//2
    if(left > right):
        return False
    
    if(arr[mid] == target):
        return True
    
    elif(arr[mid] < target):
        return recursiveBinarySearch(arr, target, mid + 1, right)

    elif(arr[mid] > target):
        return recursiveBinarySearch(arr, target, left, mid - 1)

arr = [3, 4, 6, 7, 9, 12, 16, 17]

print("Recursive Binary Search's solution: " + str(recursiveBinarySearch(arr, 12, 0, len(arr) - 1)))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------