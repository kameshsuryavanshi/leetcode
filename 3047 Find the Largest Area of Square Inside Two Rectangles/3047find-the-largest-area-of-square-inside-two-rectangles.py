from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            for j in range(i + 1, n):
                ix1 = max(bottomLeft[i][0], bottomLeft[j][0])
                iy1 = max(bottomLeft[i][1], bottomLeft[j][1])
                
                ix2 = min(topRight[i][0], topRight[j][0])
                iy2 = min(topRight[i][1], topRight[j][1])
        
                width = ix2 - ix1
                height = iy2 - iy1
        
                if width > 0 and height > 0:
                    side = min(width, height)
                    max_side = max(max_side, side)
        
        return max_side * max_side