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