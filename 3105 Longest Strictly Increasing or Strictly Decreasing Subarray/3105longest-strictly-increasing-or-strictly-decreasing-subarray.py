class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        if n <= 1:
            return n

        max_len = 1

        for i in range(n):
            curr_len = 1
            # Check increasing
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    curr_len += 1
                else:
                    break
            max_len = max(max_len, curr_len)

            curr_len = 1  # Reset for decreasing check
            # Check decreasing 
            for j in range(i + 1, n):  
                if nums[j] < nums[j - 1]:
                    curr_len += 1
                else:
                    break
            max_len = max(max_len, curr_len)

        return max_len