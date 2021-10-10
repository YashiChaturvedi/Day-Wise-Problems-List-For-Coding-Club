class Solution:
    def countFriendsPairings(self, n):
        if (n == 1 or n == 2):
            return n

        # For storing answers to the subproblems.
        dp = [0 for i in range(n + 1)]
    
        dp[1] = 1
        dp[2] = 2
    
        mod = 1e9 + 7
    
        # Iterating and calculating for every value of i = 3 to N.
        for i in range(3, n + 1):
    
            dp[i] = (dp[i - 1] + ((i - 1) * dp[i - 2]) % mod) % mod
    
        return int(dp[n])
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends
