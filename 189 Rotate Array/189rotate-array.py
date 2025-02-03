class Solution(object):
    def rotate(self, nums, k):
        """Rotates an array in-place."""
        n = len(nums)
        k %= n  # Efficiently handle k > n

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(nums, 0, n - 1)  # Reverse whole array
        reverse(nums, 0, k - 1)  # Reverse first k elements
        reverse(nums, k, n - 1)  # Reverse rest