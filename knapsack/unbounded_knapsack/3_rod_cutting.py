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
#             if(i==0 or j==0):
#                 t[i][j] = 0
            
#             if(i>0 and j>0 and length[i-1] <= j):
#                 t[i][j] = max(price[i-1] + t[i][j - length[i-1]], t[i-1][j])
            
#             elif(i>0 and j>0 and length[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[N][n]

# print(f"Rod cutting solution: {rod_cutting(length, price, n)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------