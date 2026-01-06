class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0

        # Bucket size and count
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        buckets_min = [float('inf')] * num_buckets
        buckets_max = [-float('inf')] * num_buckets

        # Fill buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)

        max_gap = 0
        prev_bucket_max = None

        for i in range(num_buckets):
            if buckets_min[i] == float('inf'):
                continue

            if prev_bucket_max is not None:
                max_gap = max(max_gap, buckets_min[i] - prev_bucket_max)

            prev_bucket_max = buckets_max[i]

        return max_gap
