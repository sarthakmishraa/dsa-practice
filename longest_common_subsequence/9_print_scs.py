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