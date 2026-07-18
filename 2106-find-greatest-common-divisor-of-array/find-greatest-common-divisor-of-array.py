
class Solution:
    def findGCD(self, nums):
        min_ = min(nums)
        max_ = max(nums)
        
        for i in range(min_, 1, -1):
            if not max_ % i and not min_ % i:
                return i
            
        return 1