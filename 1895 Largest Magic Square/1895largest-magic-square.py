class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize prefix sum arrays with padding for easy indexing
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)] # Main \
        diag2 = [[0] * (n + 1) for _ in range(m + 1)] # Anti /
        
        for r in range(m):
            for c in range(n):
                row_sum[r][c+1] = row_sum[r][c] + grid[r][c]
                col_sum[r+1][c] = col_sum[r][c] + grid[r][c]
                diag1[r+1][c+1] = diag1[r][c] + grid[r][c]
                diag2[r+1][c] = diag2[r][c+1] + grid[r][c]

        def is_magic(r, c, k):
            # Target sum from the first row of the k x k square
            target = row_sum[r][c + k] - row_sum[r][c]
            
            # Check rows
            for i in range(r + 1, r + k):
                if row_sum[i][c + k] - row_sum[i][c] != target:
                    return False
            
            # Check columns
            for j in range(c, c + k):
                if col_sum[r + k][j] - col_sum[r][j] != target:
                    return False
            
            # Check Main Diagonal \
            if diag1[r + k][c + k] - diag1[r][c] != target:
                return False
            
            # Check Anti-Diagonal /
            if diag2[r + k][c] - diag2[r][c + k] != target:
                return False
            
            return True

        # Try side length k from max possible down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1