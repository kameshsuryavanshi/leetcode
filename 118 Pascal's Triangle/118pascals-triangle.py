from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            # 1. Initialize the row with None or 1s (Size of row is i + 1)
            row = [1] * (i + 1)
            
            # 2. Calculate middle elements (only if i > 1)
            for j in range(1, i):
                # The element is sum of two elements directly above it
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            # 3. Add the row to the triangle
            triangle.append(row)
            
        return triangle