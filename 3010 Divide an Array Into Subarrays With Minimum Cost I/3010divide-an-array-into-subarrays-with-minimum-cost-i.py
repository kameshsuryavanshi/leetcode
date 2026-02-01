# class Solution:
#     def minimumCost(self, nums: List[int]) -> int:
#         n = len(nums)
#         first_c = nums[0]
#         min_c = float('inf')
#         for i in range(1,n-1):
#             for j in range(i+1,n):
#                 c = first_c + nums[i] + nums[j]
#                 min_c = min(min_c , c)
#         return min_c

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        first = nums[0]
        rest = nums[1:]
        rest.sort()
        
        return first + rest[0] + rest[1]