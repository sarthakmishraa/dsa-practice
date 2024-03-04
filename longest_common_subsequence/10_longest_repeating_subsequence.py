# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Length of longest repeating subsequence

# # str1 = 'letsleetcode'
# str1 = 'AABEBCDD'

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