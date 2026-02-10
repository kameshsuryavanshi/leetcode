class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_l = 0
        
        for i in range(n):
            # Track distinct even and odd numbers for this specific starting point
            even_nums = set()
            odd_nums = set()
            
            for j in range(i, n):
                val = nums[j]
                
                # Check if even or odd and add to the respective distinct set
                if val % 2 == 0:
                    even_nums.add(val)
                else:
                    odd_nums.add(val)
                
                # If the number of distinct even == number of distinct odd
                if len(even_nums) == len(odd_nums):
                    max_l = max(max_l, j - i + 1)
                    
        return max_l
        