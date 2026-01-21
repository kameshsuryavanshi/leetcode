from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            temp = n
            count = 0
            while temp & 1:
                temp >>= 1
                count += 1
            res = n - (1 << (count - 1))
            ans.append(res)
            
        return ans