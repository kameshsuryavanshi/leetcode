class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        res = []
        for n in nums:
            if n == 2:
                res.append(-1)
            else:
                for i in range(31):
                    if not (n & (1 << i)):
                        res.append(n ^ (1 << (i - 1)))
                        break
        return res