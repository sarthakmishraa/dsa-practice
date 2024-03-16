# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# Palindrome Partition Recursive

string1 = "nitin"
string2 = "a"
string3 = "ab"
string4 = "aab"
# string5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

def palindromePartition(string):
    t = [[-1 for _ in range(len(string) + 1)] for _ in range(len(string) + 1)]
    
    def isPalindrome(string, i, j):
        s = string[i:j+1]
        return s == s[::-1]
    
    def helper(string, t, i, j):
        res = len(string)
        
        if i>=j or isPalindrome(string, i, j):
            return 0
            
        if t[i][j] != -1:
            return t[i][j]
        
        for k in range(i, j):
            if t[i][k] != -1:
                left = t[i][k]
            else:
                left = helper(string, t, i, k)
            
            if t[k+1][j] != -1:
                right = t[k+1][j]
            else:
                right = helper(string, t, k+1, j)
                
            temp = left + right + 1
            res = min(res, temp)

        t[i][j] = res
        return t[i][j]
    
    return helper(string, t, 0, len(string)-1)

print(f"Minimum no of partitions to make all subarrays palindrome: {palindromePartition(string1)}")
print(f"Minimum no of partitions to make all subarrays palindrome: {palindromePartition(string2)}")
print(f"Minimum no of partitions to make all subarrays palindrome: {palindromePartition(string3)}")
print(f"Minimum no of partitions to make all subarrays palindrome: {palindromePartition(string4)}")
# print(f"Minimum no of partitions to make all subarrays palindrome: {palindromePartition(string5)}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------