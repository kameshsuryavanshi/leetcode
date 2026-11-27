class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = float('inf')
        
        for factor, price in items:
            mn = min(mn, price)
            cnt = sum(1 for f_j, _ in items if f_j % factor == 0)
            
            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)
        
        return max(x + (budget - i) // mn for i, x in enumerate(f))   