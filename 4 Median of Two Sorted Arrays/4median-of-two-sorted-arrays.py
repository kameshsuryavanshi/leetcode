class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Get the max element on the left side of partition in both arrays
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            
            # Get the min element on the right side of partition in both arrays
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we've found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    # Even total length, take average of two middle elements
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    # Odd total length, take the maximum of left side
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # Move left partition of nums1 to the left
                right = partition1 - 1
            else:
                # Move left partition of nums1 to the right
                left = partition1 + 1
        
        # Should never reach here
        raise ValueError("Input arrays are not sorted or invalid")