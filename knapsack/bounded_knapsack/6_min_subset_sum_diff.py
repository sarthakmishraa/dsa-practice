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