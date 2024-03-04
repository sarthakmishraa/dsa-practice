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

# # str1 = 'abcdaf'
# # str2 = 'acbcf'

# # str1 = 'abac'
# # str2 = 'cab'

# str1 = 'bbbaaaba'
# str2 = 'bbababbb'

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