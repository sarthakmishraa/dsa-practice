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