class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in n_map:
                return [n_map[comp],i]
            n_map[num] = i 
        return []
