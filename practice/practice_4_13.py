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
#         t[n][w] = max(val[n-1] + knapsack_recursive(wt, val, w-wt[n-1], n-1), knapsack_recursive(wt, val, w, n-1))
#         return t[n][w]
    
#     elif(wt[n-1] > w):
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
            
#             if(wt[i-1] <= j):
#                 t[i][j] = max(val[i-1] + t[i-1][j - wt[i-1]], t[i-1][j])
            
#             elif(wt[i-1] > j):
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
#                 t[i][j] = t[i-1][j - nums[i-1]] or t[i-1][j]
            
#             elif(i>0 and j>0 and nums[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
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
#     sum_val = sum(nums)//2
    
#     def subset_sum(nums, sum_val):
#         n = len(nums)
        
#         t = [[None for _ in range(sum_val + 1)] for _ in range(n + 1)]
        
#         for i in range(n + 1):
#             for j in range(sum_val + 1):
#                 if(i==0 and j==0):
#                     t[i][j] = True
                
#                 elif(i==0 and j!=0):
#                     t[i][j] = True
                
#                 elif(i!=0 and j==0):
#                     t[i][j] = False
                
#                 if(i>0 and j>0 and nums[i-1] <= j):
#                     t[i][j] = t[i-1][j - nums[i-1]] or t[i-1][j]
                
#                 elif(i>0 and j>0 and nums[i-1] > j):
#                     t[i][j] = t[i-1][j]
        
#         return t[n][sum_val]
    
#     if(sum(nums)%2 != 0):
#         return False
        
#     return subset_sum(nums, sum_val)

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
#     s2 = sum(nums) - s1
    
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
    
#     s1 = (sum(nums) + diff)//2
#     return subset_sum(nums, s1)
    
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
    
#     s1 = (sum(nums) + target)//2
    
#     return subset_sum(nums, s1)

# print(f"Target sum solution for nums1: {target_sum(nums1, target1)}")
# print(f"Target sum solution for nums2: {target_sum(nums2, target2)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # unbounded knapsack recursive

# wt = [1, 2, 3, 5]

# val = [3, 5, 6 ,8]

# w = 5

# n = len(wt)

# t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

# def unbounded_knapsack_recursive(wt, val, n, w):
#     if(n==0 or w==0):
#         return 0
    
#     if(t[n][w] != 0):
#         return t[n][w]
    
#     if(wt[n-1] <= w):
#         t[n][w] = max(val[n-1] + unbounded_knapsack_recursive(wt, val, n, w - wt[n-1]), unbounded_knapsack_recursive(wt, val, n-1, w))
#         return t[n][w]
    
#     elif(wt[n-1] > w):
#         t[n][w] = unbounded_knapsack_recursive(wt, val, n-1, w)
#         return t[n][w]

# print(f"Unbounded knapsack recursive solution: {unbounded_knapsack_recursive(wt, val, n, w)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # unbounded knapsack iterative

# wt = [1, 2, 3, 5]

# val = [3, 5, 6 ,8]

# w = 5

# def unbounded_knapsack_iterative(wt, val, w):
#     n = len(wt)
    
#     t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(w + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and wt[i-1] <= j):
#                 t[i][j] = max(val[i-1] + t[i][j - wt[i-1]], t[i-1][j])
            
#             elif(i>0 and j>0 and wt[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][w]

# print(f"Unbounded knapsack iterative solution: {unbounded_knapsack_iterative(wt, val, w)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # rod cutting problem

# length = [1, 2, 3, 4, 5, 6, 7, 8]

# price = [1, 5, 8, 9, 10, 17, 17, 20]

# n = 8

# def rod_cutting(length, price, n):
#     N = len(length)
    
#     t = [[0 for _ in range(n + 1)] for _ in range(N + 1)]
    
#     for i in range(N + 1):
#         for j in range(n + 1):
#             if(i==0 and j==0):
#                 t[i][j] = 1
            
#             elif(i!=0 and j==0):
#                 t[i][j] = 1
            
#             elif(i==0 and j!=0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and length[i-1] <= j):
#                 t[i][j] = max(price[i-1] + t[i][j - length[i-1]], t[i-1][j])
            
#             elif(i>0 and j>0 and length[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[N][n]

# print(f"Rod cutting solution: {rod_cutting(length, price, n)}")

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

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of longest common subsequence recursive

# x = 'abcef'
# y = 'abhjf'

# n = len(x)
# m = len(y)

# t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# def lcs_recursive(x, y, n, m):
#     if(n==0 or m==0):
#         return 0
        
#     if(t[n][m] != 0):
#         return t[n][m]
    
#     if(x[n-1] == y[m-1]):
#         t[n][m] = 1 + lcs_recursive(x, y, n-1, m-1)
#         return t[n][m]
    
#     else:
#         t[n][m] = max(lcs_recursive(x, y, n-1, m), lcs_recursive(x, y, n, m-1))
#         return t[n][m]
    
# print(f"Length of longest common subsequence's solution: {lcs_recursive(x, y, n, m)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of longest common subsequence iterative

# x = 'abcef'
# y = 'abhjf'

# def lcs_iterative(x, y):
#     n = len(x)
#     m = len(y)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and x[i-1] == y[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and x[i-1] != y[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return t[n][m]

# print(f"Length of longest common subsequence iterative solution: {lcs_iterative(x, y)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Longest common substring

# str1 = 'abcde'
# str2 = 'abfce'

# def longest_common_substring(str1, str2):
#     n = len(str1)
#     m = len(str2)
    
#     res = 0
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
#                 res = max(res, t[i][j])
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = 0
    
#     return res

# print(f"Length of longest common substring solution: {longest_common_substring(str1, str2)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Printing longest common subsequence

# # x = 'acbggacf'
# # y = 'ggb'

# x = 'acbcf'
# y = 'abcdaf'

# def lcs_print(x, y):
#     n = len(x)
#     m = len(y)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and x[i-1] == y[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and x[i-1] != y[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     i = n
#     j = m
#     res = ""
    
#     while(i>0 and j>0):
#         if(x[i-1] == y[j-1]):
#             res = res + x[i-1]
#             i = i-1
#             j = j-1
        
#         else:
#             if(t[i-1][j] > t[i][j-1]):
#                 i = i-1
            
#             else:
#                 j = j-1
    
#     return res[::-1]

# print(f"Longest common subsequence is {lcs_print(x, y)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of shortest common supersequence

# x = 'AGGTAB'
# y = 'GXTXAYB'

# def scs_length(x, y):
#     n = len(x)
#     m = len(y)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and x[i-1] == y[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and x[i-1] != y[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return n + m - t[n][m]

# print(f"Length of shortest common supersequence is {scs_length(x, y)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # No of insertions and deletions to convert a string A to a string B

# x = 'heap'
# y = 'pea'

# def ins_del_to_convert_A_to_B(x, y):
#     n = len(x)
#     m = len(y)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and x[i-1] == y[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and x[i-1] != y[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     insertions = m - t[n][m]
#     deletions = n - t[n][m]
    
#     return insertions, deletions

# insertions, deletions = ins_del_to_convert_A_to_B(x, y)

# print(f"insertions: {insertions}, Deletions: {deletions}\nSo total no of modifications are: {insertions + deletions}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of longest Palindromic Subsequence

# str1 = 'agbcba'

# def len_of_longest_palindromic_sequence(str1):
#     str2 = str1[::-1]
    
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return t[n][m]

# print(f"Length of longest palindromic subsequence: {len_of_longest_palindromic_sequence(str1)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Longest Palindromic Subsequence

# str1 = 'agbcba'

# def longest_palindromic_sequence(str1):
#     str2 = str1[::-1]
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     i = n
#     j = m
#     res = ""
    
#     while(i>0 and j>0):
#         if(str1[i-1] == str2[j-1]):
#             res = res + str1[i-1]
#             i = i-1
#             j = j-1
        
#         else:
#             if(t[i-1][j] > t[i][j-1]):
#                 i = i-1
            
#             else:
#                 j = j-1
    
#     return res[::-1]

# print(f"Longest palindromic subsequence is: {longest_palindromic_sequence(str1)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Printing Shortest Common Supersequence

# str1 = 'abcdaf'
# str2 = 'acbcf'

# # str1 = 'abac'
# # str2 = 'cab'

# # str1 = 'bbbaaaba'
# # str2 = 'bbababbb'

# # str1 = 'bbabacaa'
# # str2 = 'cccababab'

# def scs_print(str1, str2):
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     i = n
#     j = m
#     res = ""
    
#     while(i>0 and j>0):
#         if(str1[i-1] == str2[j-1]):
#             res = res + str1[i-1]
#             i = i-1
#             j = j-1
        
#         else:
#             if(t[i-1][j] > t[i][j-1]):
#                 res = res + str1[i-1]
#                 i = i-1
            
#             else:
#                 res = res + str2[j-1]
#                 j = j-1
    
#     while(i>0):
#         res = res + str1[i-1]
#         i = i-1
    
#     while(j>0):
#         res = res + str2[j-1]
#         j = j-1
    
#     return res[::-1]

# print(f"Shortest common supersequence is: {scs_print(str1, str2)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of longest repeating subsequence

# str1 = 'letsleetcode'
# # str1 = 'AABEBCDD'

# def longest_repeating_subsequence(str1):
#     str2 = str1
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1] and i!=j):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             else:
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return t[n][m]

# print(f"Length of longest repeating subsequence solution: {longest_repeating_subsequence(str1)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Sequence pattern matching

# str1 = 'AXY'
# str2 = 'ADXCPY'

# # str1 = "abc"
# # str2 = "ahbgdc"

# def isSubsequence(str1, str2):
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return t[n][m] == n

# print(f"Sequence pattern matching solution: {isSubsequence(str1, str2)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Minimum number of insertion in a string to make it a palindrome

# str1 = 'acbcbda'

# def ins_to_make_palindrome(str1):
#     str2 = str1[::-1]
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
            
#             elif(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = max(t[i-1][j], t[i][j-1])
    
#     return n - t[n][m]

# print(f"Minimum number of insertion in a string to make it a palindrome solution: {ins_to_make_palindrome(str1)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------