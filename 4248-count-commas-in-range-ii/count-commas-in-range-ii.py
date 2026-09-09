class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        p = 1000  
        while p <= n:
            total += n - p + 1  
            p *= 1000  
            
        return total