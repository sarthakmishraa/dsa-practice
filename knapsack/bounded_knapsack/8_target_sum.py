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