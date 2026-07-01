from typing import List
import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        max_heap = [(-dist[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        while max_heap:
            safeness, r, c = heapq.heappop(max_heap)
            safeness = -safeness  

            if r == n - 1 and c == n - 1:
                return safeness
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    new_safeness = min(safeness, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safeness, nr, nc))
        
        return 0