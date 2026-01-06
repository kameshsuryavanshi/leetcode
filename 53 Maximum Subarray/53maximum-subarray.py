# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_s = nums
#         current_sum = nums
#         for i in range (1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])        
#             max_s = max(max_s,current_sum)
#         return max_s

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the existing subarray or start fresh
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum
