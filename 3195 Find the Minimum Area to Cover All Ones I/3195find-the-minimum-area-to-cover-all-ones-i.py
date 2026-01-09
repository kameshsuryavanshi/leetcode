class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        if rows == 0: return 0
        cols = len(grid[0]) # Fix 1: Properly get column count
        
        # Initialize boundaries
        top, bottom = float('inf'), float('-inf')
        left, right = float('inf'), float('-inf')
        
        found_one = False
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    found_one = True
                    top = min(top, r)
                    bottom = max(bottom, r)
                    left = min(left, c)
                    right = max(right, c)
        
        # Fix 2 & 3: Handle empty grid and calculate area
        if not found_one:
            return 0
            
        height = bottom - top + 1
        width = right - left + 1
        
        return height * width