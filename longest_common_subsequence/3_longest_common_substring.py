# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # Longest common substring

# str1 = 'abcde'
# str2 = 'abfce'

# def longest_common_substring(str1, str2):
#     n = len(str1)
#     m = len(str2)
    
#     t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
#     res = 0
    
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and str1[i-1] == str2[j-1]):
#                 t[i][j] = 1 + t[i-1][j-1]
#                 res = max(res, t[i][j])
            
#             if(i>0 and j>0 and str1[i-1] != str2[j-1]):
#                 t[i][j] = 0
    
#     return res

# print(f"Length of longest common substring solution: {longest_common_substring(str1, str2)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------