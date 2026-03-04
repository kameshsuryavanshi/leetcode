from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
        
        # Initialize row and column sum arrays
        row_sums = [0] * num_rows
        col_sums = [0] * num_cols
        
        # Calculate sums
        for i in range(num_rows):
            for j in range(num_cols):
                value = mat[i][j]
                row_sums[i] += value
                col_sums[j] += value
        
        # Count special positions
        special_count = 0
        
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
        
        return special_count