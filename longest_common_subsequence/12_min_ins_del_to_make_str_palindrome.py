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