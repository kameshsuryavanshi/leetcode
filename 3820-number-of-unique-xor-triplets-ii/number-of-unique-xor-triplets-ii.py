from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        global_unique = set()
        suffix_pair_xor = set()
        n = len(nums)
        
        for i in range(n - 1, -1, -1):
            new_pairs = set()
            for k in range(i, n):
                new_pairs.add(nums[i] ^ nums[k])
            
            suffix_pair_xor.update(new_pairs)
            
            for val in suffix_pair_xor:
                global_unique.add(nums[i] ^ val)
        
        return len(global_unique)