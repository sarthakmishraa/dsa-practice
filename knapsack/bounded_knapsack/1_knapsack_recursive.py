# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# # knapsack one zero recursive

# wt = [1, 3, 4 ,7]

# val = [2, 4, 6, 8]

# w = 7

# n = len(wt)

# t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

# def knapsack_recursive(wt, val, w, n):
#     if(w==0 or n==0):
#         return 0
    
#     if(t[n][w] != 0):
#         return t[n][w]
    
#     if(wt[n-1] <= w):
#         t[n][w] = max(val[n-1] + knapsack_recursive(wt, val, w - wt[n-1], n-1), knapsack_recursive(wt, val, w, n-1))
#         return t[n][w]
    
#     else:
#         t[n][w] = knapsack_recursive(wt, val, w, n-1)
#         return t[n][w]
    
# print(f"Knapsack zero one recursive solution: {knapsack_recursive(wt, val, w, n)}")
    
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------