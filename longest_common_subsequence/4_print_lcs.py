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