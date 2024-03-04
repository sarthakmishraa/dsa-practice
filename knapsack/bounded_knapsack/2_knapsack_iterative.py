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
            
#             if(i>0 and j>0 and wt[i-1] <= j):
#                 t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
                
#             elif(i>0 and j>0 and wt[i-1] > j):
#                 t[i][j] = t[i-1][j]
    
#     return t[n][w]
            
# print(f"Knapsack zero one iterative solution: {knapsack_iterative(wt, val, w)}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------