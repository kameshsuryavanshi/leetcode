from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, float('inf')])
        
        m = len(restrictions)
        
        for i in range(1, m):
            idx_diff = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + idx_diff)
            
        for i in range(m - 2, -1, -1):
            idx_diff = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + idx_diff)
            
        max_h = 0
        
        for i in range(m - 1):
            idx1, h1 = restrictions[i]
            idx2, h2 = restrictions[i+1]    
            dist = idx2 - idx1
            current_max = (h1 + h2 + dist) // 2
            max_h = max(max_h, current_max)
            
        return max_h