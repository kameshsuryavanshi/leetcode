class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Step 1: Get lengths
        m, n = len(s), len(t)

        # Step 2: Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1  # Empty t matches any s prefix

        # Step 3: Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]
        