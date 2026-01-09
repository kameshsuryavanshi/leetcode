class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # Create a 2D DP table (m+1 rows x n+1 columns)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True 
        
        # Handle patterns like a*, a*b*, or .* for empty string 's'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                    )
                else:
                    # Current characters match or pattern has a dot
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        
        return dp[m][n]