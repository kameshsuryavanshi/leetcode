from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        
        min_cost = [[float('inf')] * COLS for _ in range(ROWS)]
        
        start_cost = grid[0][0]
        min_cost[0][0] = start_cost
        
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            if r == ROWS - 1 and c == COLS - 1:
                break
                
            current_cost = min_cost[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    next_cost = current_cost + grid[nr][nc]
                    
                    if next_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = next_cost
                        
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                   
        return min_cost[ROWS - 1][COLS - 1] < health