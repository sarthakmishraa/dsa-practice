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