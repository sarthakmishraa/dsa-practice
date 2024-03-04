# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# # unbounded knapsack recursive

# wt = [1, 2, 3, 5]

# val = [3, 5, 6 ,8]

# w = 5

# n = len(wt)

# t = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

# def unbounded_knapsack_recursive(wt, val, n, w):
    
#     if(w==0 or n==0):
#         return 0
    
#     if(t[n][w] != 0):
#         return t[n][w]
    
#     if(wt[n-1] <= w):
#         t[n][w] = max(val[n-1] + unbounded_knapsack_recursive(wt, val, n, w - wt[n-1]), unbounded_knapsack_recursive(wt, val, n-1, w))
#         return t[n][w]
    
#     else:
#         t[n][w] = unbounded_knapsack_recursive(wt, val, n-1, w)
#         return t[n][w]

# print(f"Unbounded knapsack recursive solution: {unbounded_knapsack_recursive(wt, val, n, w)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
