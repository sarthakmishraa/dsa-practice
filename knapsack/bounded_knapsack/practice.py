# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # knapsack one zero recursive

# wt = [1, 3, 4 ,7]

# val = [2, 4, 6, 8]

# w = 7

# n = len(wt)

# t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

# def knapsack_recursive(wt, val, w, n):
#     if(w==0 or n==0):
#         return 0
    
#     if(t[n][w] != 0):
#         return t[n][w]
    
#     if(wt[n-1] <= w):
#         t[n][w] = max(val[n-1] + knapsack_recursive(wt, val, w - wt[n-1], n-1), knapsack_recursive(wt, val, w, n-1))
#         return t[n][w]
    
#     else:
#         t[n][w] = knapsack_recursive(wt, val, w, n-1)
#         return t[n][w]
    
# print(f"Knapsack zero one recursive solution: {knapsack_recursive(wt, val, w, n)}")
    
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # knapsack one zero iterative

# wt = [1, 3, 4 ,7]

# val = [2, 4, 6, 8]

# w = 7

# def knapsack_iterative(wt, val, w):
#     n = len(wt)
    
#     t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(w + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and wt[i-1] <= j):
#                 t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
                
#             elif(i>0 and j>0 and wt[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][w]
            
# print(f"Knapsack zero one iterative solution: {knapsack_iterative(wt, val, w)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # subset sum yes or no

# nums = [2, 3, 7, 8, 10]

# sum_val = 11

# def subset_sum(nums, sum_val):
#     n = len(nums)
    
#     t = [[None for _ in range(sum_val + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(sum_val + 1):
#             if(i==0 and j==0):
#                 t[i][j] = True
            
#             elif(i!=0 and j==0):
#                 t[i][j] = True
            
#             elif(i==0 and j!=0):
#                 t[i][j] = False
            
#             if(i>0 and j>0 and nums[i-1] <= j):
#                 t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
            
#             elif(i>0 and j>0 and nums[i-1] > j):
#                 t[i][j] = t[i-1][n]
    
#     return t[n][sum_val]

# print(f"Subset sum solution: {subset_sum(nums, sum_val)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # equal sum

# nums1 = [1,5,11,5]
# # True

# nums2 = [1,2,3,5]
# # False

# nums3 = [1, 5, 11, 5, 6, 6, 8, 9]
# # False

# nums4 = [1, 5, 11, 5, 6, 6, 8, 9, 1]
# # True

# def equal_sum(nums):
#     n = len(nums)
    
#     if(sum(nums)%2 != 0):
#         return False
        
#     sum_val = sum(nums)//2
    
#     t = [[None for _ in range(sum_val + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(sum_val + 1):
#             if(i==0 and j==0):
#                 t[i][j] = True
            
#             elif(i!=0 and j==0):
#                 t[i][j] = True
            
#             elif(i==0 and j!=0):
#                 t[i][j] = False
            
#             if(i>0 and j>0 and nums[i-1] <= j):
#                 t[i][j] = t[i-1][j - nums[i-1]] or t[i-1][j]
            
#             elif(i>0 and j>0 and nums[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][sum_val]

# print(f"Equal sum solution for nums1: {equal_sum(nums1)}")
# print(f"Equal sum solution for nums2: {equal_sum(nums2)}")
# print(f"Equal sum solution for nums3: {equal_sum(nums3)}")
# print(f"Equal sum solution for nums4: {equal_sum(nums4)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # count of subset sum

# nums = [2, 3, 5, 6, 8, 10]

# sum_val = 10

# def count_of_subset_sum(nums, sum_val):
#     n = len(nums)
    
#     t = [[0 for _ in range(sum_val + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(sum_val + 1):
#             if(i==0 and j==0):
#                 t[i][j] = 1
            
#             elif(i!=0 and j==0):
#                 t[i][j] = 1
            
#             elif(i==0 and j!=0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and nums[i-1] <= j):
#                 t[i][j] = t[i-1][j - nums[i-1]] + t[i-1][j]
            
#             elif(i>0 and j>0 and nums[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][sum_val]

# print(f"Count of subset sum solution: {count_of_subset_sum(nums, sum_val)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # minimum subset sum difference

# nums1 = [1, 2, 7]
# nums2 = [3, 9 ,7 ,3]

# def min_subset_sum_diff(nums):
    
#     sum_val = sum(nums)
    
#     def subset_sum_modified(nums, sum_val):
#         n = len(nums)
#         t = [[None for _ in range(sum_val + 1)] for _ in range(n + 1)]
        
#         for i in range(n + 1):
#             for j in range(sum_val + 1):
#                 if(i==0 and j==0):
#                     t[i][j] = True
                
#                 elif(i!=0 and j==0):
#                     t[i][j] = True
                
#                 elif(i==0 and j!=0):
#                     t[i][j] = False
                
#                 if(i>0 and j>0 and nums[i-1] <= j):
#                     t[i][j] = t[i-1][j - nums[i-1]] or t[i-1][j]
                
#                 elif(i>0 and j>0 and nums[i-1] > j):
#                     t[i][j] = t[i-1][j]
                
#         return t[n]
    
#     temp = subset_sum_modified(nums, sum_val)
#     temp2 = []
    
#     for i in range(len(temp)//2):
#         if temp[i]:
#             temp2.append(i)
    
#     s1 = temp2[-1]
#     s2 = sum_val - s1
    
#     return abs(s1 - s2)

# print(f"Minimum subset sum difference solution for nums1: {min_subset_sum_diff(nums1)}")
# print(f"Minimum subset sum difference solution for nums2: {min_subset_sum_diff(nums2)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # no of subset with a given difference

# nums = [1, 1, 2, 3]

# diff = 1

# def count_of_subset_sum_with_diff(nums, diff):
    
#     def subset_sum(nums, sum_val):
#         n = len(nums)
        
#         t = [[0 for _ in range(sum_val + 1)] for _ in range(n + 1)]
        
#         for i in range(n + 1):
#             for j in range(sum_val + 1):
#                 if(i==0 and j==0):
#                     t[i][j] = 1
                
#                 elif(i!=0 and j==0):
#                     t[i][j] = 1
                
#                 elif(i==0 and j!=0):
#                     t[i][j] = 0
                
#                 if(i>0 and j>0 and nums[i-1] <= j):
#                     t[i][j] = t[i-1][j - nums[i-1]] + t[i-1][j]
                
#                 elif(i>0 and j>0 and nums[i-1] > j):
#                     t[i][j] = t[i-1][j]
        
#         return t[n][sum_val]
    
#     sum_val = (sum(nums) + diff)//2
    
#     return subset_sum(nums, sum_val)

# print(f"Count of subset sum with given difference solution: {count_of_subset_sum_with_diff(nums, diff)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # target sum

# nums1 = [1, 1, 2, 3]
# target1 = 1

# nums2 = [1,1,1,1,1]
# target2 = 3

# def target_sum(nums, target):
    
#     def subset_sum(nums, sum_val):
#         n = len(nums)
        
#         t = [[0 for _ in range(sum_val + 1)] for _ in range(n + 1)]
        
#         for i in range(n + 1):
#             for j in range(sum_val + 1):
#                 if(i==0 and j==0):
#                     t[i][j] = 1
                    
#                 elif(i!=0 and j==0):
#                     t[i][j] = 1
                
#                 elif(i==0 and j!=0):
#                     t[i][j] = 0
                
#                 if(i>0 and j>0 and nums[i-1] <= j):
#                     t[i][j] = t[i-1][j - nums[i-1]] + t[i-1][j]
                
#                 elif(i>0 and j>0 and nums[i-1] > j):
#                     t[i][j] = t[i-1][j]
        
#         return t[n][sum_val]
    
#     sum_val = ((sum(nums) + target))//2
    
#     return subset_sum(nums, sum_val)

# print(f"Target sum solution for nums1: {target_sum(nums1, target1)}")
# print(f"Target sum solution for nums2: {target_sum(nums2, target2)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------