from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        nodes = list(set(original) | set(changed))
        node_to_id = {s: i for i, s in enumerate(nodes)}
        m = len(nodes)
        
        inf = float('inf')
        dist = [[inf] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        for u_s, v_s, c in zip(original, changed, cost):
            u, v = node_to_id[u_s], node_to_id[v_s]
            if c < dist[u][v]:
                dist[u][v] = c
            
        for k in range(m):
            for i in range(m):
                if dist[i][k] == inf: continue
                for j in range(m):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        valid_lengths = sorted(list(set(len(s) for s in nodes)))
        
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            for l in valid_lengths:
                if i + l > n:
                    break
                
                sub_s = source[i:i+l]
                sub_t = target[i:i+l]
                
                if sub_s in node_to_id and sub_t in node_to_id:
                    u, v = node_to_id[sub_s], node_to_id[sub_t]
                    if dist[u][v] != inf:
                        if dp[i] + dist[u][v] < dp[i+l]:
                            dp[i+l] = dp[i] + dist[u][v]
                        
        return dp[n] if dp[n] != inf else -1