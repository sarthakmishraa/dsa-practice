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