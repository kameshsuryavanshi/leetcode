from sortedcontainers import SortedList
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))       
        busy = []
        cnt = [0] * k
        
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                end_time, server_id = heapq.heappop(busy)
                free.add(server_id)
            if not free:
                continue
            idx = free.bisect_left(i % k)
            if idx == len(free):
                idx = 0
            
            server = free[idx]
            cnt[server] += 1
            
            heapq.heappush(busy, (start + t, server))
            free.remove(server)
            
        mx = max(cnt)
        return [i for i, v in enumerate(cnt) if v == mx]   