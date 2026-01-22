class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        while not self.isNonDecreasing(nums):
            # Find the leftmost pair with minimum sum
            min_sum = float('inf')
            min_index = 0
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_index = i
            
            # Replace the pair with their sum
            nums[min_index] = min_sum
            nums.pop(min_index + 1)
            operations += 1
        
        return operations
    
    def isNonDecreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True