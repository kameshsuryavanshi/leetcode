class Solution:
    def minElement(self, nums):
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        return min(digit_sum(x) for x in nums)