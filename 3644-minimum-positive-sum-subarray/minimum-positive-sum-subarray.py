class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                if length > r:
                    break
                if length >= l and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return -1 if min_sum == float('inf') else min_sum   