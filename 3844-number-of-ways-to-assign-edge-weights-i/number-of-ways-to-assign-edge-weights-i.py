from collections import defaultdict
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        max_depth = 0
        
        def dfs(node, parent, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)
        
        dfs(1, -1, 0)
    
        MOD = 10**9 + 7
      
        return pow(2, max_depth - 1, MOD)