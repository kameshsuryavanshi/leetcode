class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, number in enumerate(nums):
            digit_sum = 0
            temp_number = number

            while temp_number > 0:
                digit_sum += temp_number % 10
                temp_number //= 10

            if digit_sum == index: 
                return index

        return -1