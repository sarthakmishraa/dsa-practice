# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# recursive binary search

def recursiveBinarySearch(arr, target, left, right):
    pass

arr = [3, 4, 6, 7, 9, 12, 16, 17]

print("Recursive Binary Search's solution: " + str(recursiveBinarySearch(arr, 12, 0, len(arr) - 1)))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# iterative binary search

def iterativeBinarySearch(arr, target):
    pass

arr = [3, 4, 6, 7, 9, 12, 16, 17]

print("Recursive Binary Search's solution: " + str(iterativeBinarySearch(arr, 12)))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Finding lower bound
# a lower bound is smallest index such that arr[index] >= n

# in easy words
# find the element (arr[index]) in the array that is >= n, then get its index
# if there are multiple elements with the same value, return the smallest index

arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]

def lowerBound(arr, x):
    pass
    
print("The lower bound for 1 is:", lowerBound(arr, 1))
print("The lower bound for 9 is:", lowerBound(arr, 9))
print("The lower bound for 6 is:", lowerBound(arr, 6))
print("The lower bound for 10 is:", lowerBound(arr, 10))

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
    pass

arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
print("The upper bound for 6 is:", upperBound(arr, 6))
print("The upper bound for 11 is:", upperBound(arr, 11))
print("The upper bound for 12 is:", upperBound(arr, 12))
print("The upper bound for 13 is:", upperBound(arr, 13))
print("The upper bound for 0 is:", upperBound(arr, 0))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# search insert positon

def searchInsertBinarySearch(arr, target):
    pass
    
def searchInsertBinarySearchWithLowerBound(arr, target):
    pass

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

# Floor value

def floorBinarySearch(arr, target):
    pass
    
arr = [10, 20, 30, 40, 50]
print("Floor value for 25 is:", floorBinarySearch(arr, 25))
print("Floor value for 35 is:", floorBinarySearch(arr, 35))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Ceil value

def ceilBinarySearch(arr, target):
    pass

arr = [10, 20, 30, 40, 50]
print("Ceil value for 25 is:", ceilBinarySearch(arr, 25))
print("Ceil value for 35 is:", ceilBinarySearch(arr, 35))
print("Ceil value for 15 is:", ceilBinarySearch(arr, 15))
print("Ceil value for 20 is:", ceilBinarySearch(arr, 20))

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------