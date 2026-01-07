# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         closest_sum = float('inf')
#         min_difff = float('inf')

#         for i in range(n-1):
#             l = i +1 
#             r = n-1
#             while l <r :
#                 curr_sum = nums[i] + nums[l] + nums[r]
#                 curr_diff = abs(curr_sum - target)

#                 if curr_diff < min_difff:
#                     min_diff = curr_diff
#                     closest_sum = curr_sum
#                 if curr_sum < target:
#                     l += 1
#                 elif curr_sum > target:
#                     r -= 1
#                 else :
#                     return curr_sum 
#             return closest_sum






class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match found

        return closest_sum