from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0]) 
        
        # Build prefix sum array correctly
        # prefix[i][j] represents the sum of mat[0...i-1][0...j-1]
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + 
                               prefix[i-1][j] + 
                               prefix[i][j-1] - 
                               prefix[i-1][j-1])
        
        # Helper to get the sum of a square with side length k starting at (r, c)
        def getSquareSum(r, c, k):
            return prefix[r+k][c+k] - prefix[r][c+k] - prefix[r+k][c] + prefix[r][c]
        
        def canFind(k):
            if k == 0: return True
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if getSquareSum(i, j, k) <= threshold:
                        return True
            return False
        
        # Binary search on side length
        left, right = 1, min(m, n)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canFind(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result