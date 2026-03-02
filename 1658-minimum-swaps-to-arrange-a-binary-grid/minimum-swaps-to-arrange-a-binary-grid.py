class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        
        # Step 2: Try to place correct row at each position
        for i in range(n):
            required = n - i - 1
            
            j = i
            while j < n and trailing_zeros[j] < required:
                j += 1
            
            if j == n:
                return -1  
            
            # Step 3: Bring row j to position i
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = \
                trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
                j -= 1
        
        return swaps