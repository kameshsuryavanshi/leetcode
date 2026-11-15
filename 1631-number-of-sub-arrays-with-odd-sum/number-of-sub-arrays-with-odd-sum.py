class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        cnt = [1, 0] 
        ans = s = 0
        for x in arr:
            s = (s + x) % 2
            ans = (ans + cnt[s ^ 1]) % MOD
            cnt[s] += 1
        return ans   