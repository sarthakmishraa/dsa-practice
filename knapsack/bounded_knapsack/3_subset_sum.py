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