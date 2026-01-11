from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] 
        max_a = 0
        heights_with_sentinel = heights + [0]
        
        for i, h in enumerate(heights_with_sentinel):
            while stack[-1] != -1 and heights_with_sentinel[stack[-1]] >= h:
                height = heights_with_sentinel[stack.pop()]
               
                width = i - stack[-1] - 1
                max_a = max(max_a, height * width)
            stack.append(i)
            
        return max_a