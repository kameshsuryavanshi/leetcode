from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        for src_char, tgt_char, c in zip(original, changed, cost):
            u = ord(src_char) - ord('a')
            v = ord(tgt_char) - ord('a')
            dist[u][v] = min(dist[u][v], c)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[u][v] == inf:
                return -1
            total_cost += dist[u][v]
            
        return total_cost