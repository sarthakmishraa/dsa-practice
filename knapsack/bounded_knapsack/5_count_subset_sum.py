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