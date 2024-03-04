# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # coin change problem - maximum no of ways

# nums1 = [1, 2, 3, 5, 8, 10]
# sum_val1 = 10
# # output = 23

# nums2 = [1, 2, 3]
# sum_val2 = 5
# # output = 5

# nums3 = [1, 2, 5]
# sum_val3 = 5
# # output = 4

# nums4 = [2]
# sum_val4 = 3
# # output = 0

# nums5 = [10]
# sum_val5 = 10
# # output = 1

# def coin_change_max_ways(nums, sum_val):
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
#                 t[i][j] = t[i][j - nums[i-1]] + t[i-1][j]
            
#             elif(i>0 and j>0 and nums[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][sum_val]

# print(f"Coin change maximum no of ways solution for nums1: {coin_change_max_ways(nums1, sum_val1)}")
# print(f"Coin change maximum no of ways solution for nums2: {coin_change_max_ways(nums2, sum_val2)}")
# print(f"Coin change maximum no of ways solution for nums3: {coin_change_max_ways(nums3, sum_val3)}")
# print(f"Coin change maximum no of ways solution for nums4: {coin_change_max_ways(nums4, sum_val4)}")
# print(f"Coin change maximum no of ways solution for nums5: {coin_change_max_ways(nums5, sum_val5)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------