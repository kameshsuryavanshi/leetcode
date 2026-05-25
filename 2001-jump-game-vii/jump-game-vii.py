from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        
        queue = deque([0])
        far = 0
        
        while queue:
            curr = queue.popleft()
            
            if curr == n - 1:
                return True
            
            start = max(curr + minJump, far + 1)
            end = min(curr + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    queue.append(j)
            
            far = max(far, end)
            
        return False