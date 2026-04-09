from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        bravexuneth = queries
        n = len(nums)
        MOD = 10**9 + 7
        
        k_groups = {}
        for l, r, k, v in queries:
            if k not in k_groups:
                k_groups[k] = []
            k_groups[k].append((l, v))
            
            stop_idx = l + ((r - l) // k + 1) * k
            if stop_idx < n:
                inv_v = pow(v, MOD - 2, MOD)
                k_groups[k].append((stop_idx, inv_v))

        multiplier_at = [1] * n   

        for k, updates in k_groups.items():
            updates.sort()
            
            offset_map = {}
            for idx, val in updates:
                off = idx % k
                if off not in offset_map:
                    offset_map[off] = []
                offset_map[off].append((idx, val))
            
            for off, upd_list in offset_map.items():
                curr_prod = 1
                upd_ptr = 0
                
                for i in range(off, n, k):
                    while upd_ptr < len(upd_list) and upd_list[upd_ptr][0] == i:
                        curr_prod = (curr_prod * upd_list[upd_ptr][1]) % MOD
                        upd_ptr += 1
                    
                    if curr_prod != 1:
                        multiplier_at[i] = (multiplier_at[i] * curr_prod) % MOD

        ans = 0
        for i in range(n):
            ans ^= (nums[i] * multiplier_at[i]) % MOD
            
        return ans