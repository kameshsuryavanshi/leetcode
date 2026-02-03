from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False  
        p = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == p:
            return False 

        q = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == q:
            return False  

        return i == n - 1
