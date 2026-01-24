class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 1. Sort the array to pair smallest with largest
        nums.sort()
        
        max_sum = 0
        n = len(nums)
        
        # 2. Iterate through the first half of the array
        for i in range(n // 2):
           
            current_pair_sum = nums[i] + nums[n - 1 - i]
            
            # 3. Update the maximum pair sum found so far
            if current_pair_sum > max_sum:
                max_sum = current_pair_sum
                
        return max_sum