from typing import List
from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        LOG = 20 
        
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        def dfs(u, p, d):
            depth[u] = d
            up[u][0] = p
            for v in graph[u]:
                if v != p:
                    dfs(v, u, d + 1)
        
        dfs(1, 1, 0)
        
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            
            if u == v:
                return u
            
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            
            return up[u][0]
        
        result = []
        
        for u, v in queries:
            if u == v:
                result.append(0)
                continue
            
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            
            ways = pow(2, dist - 1, MOD)
            result.append(ways)
            
        return result