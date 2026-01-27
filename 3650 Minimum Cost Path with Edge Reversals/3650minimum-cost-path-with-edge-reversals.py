import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
            
        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]
        switch_used = [False] * n
        
        while pq:
            curr_cost, u = heapq.heappop(pq)
            
            if curr_cost > distances[u]:
                continue
            
            if u == n - 1:
                return curr_cost
            
            for v, w in adj[u]:
                if distances[v] > curr_cost + w:
                    distances[v] = curr_cost + w
                    heapq.heappush(pq, (distances[v], v))
            
            if not switch_used[u]:
                for v, w in rev_adj[u]:
                    new_cost = curr_cost + (2 * w)
                    if distances[v] > new_cost:
                        distances[v] = new_cost
                        heapq.heappush(pq, (new_cost, v))
                switch_used[u] = True
                
        return distances[n-1] if distances[n-1] != float('inf') else -1