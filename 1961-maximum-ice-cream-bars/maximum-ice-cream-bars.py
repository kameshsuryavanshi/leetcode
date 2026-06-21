from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
        ice_creams = 0
        for price in range(1, max_cost + 1):
            
            if price > coins:
                break
            
            if count[price] > 0:
                num = min(count[price], coins // price)
                ice_creams += num
                coins -= num * price
        
        return ice_creams