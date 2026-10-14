class Solution:
    def maxSumOfSquares(self, num: int, total: int) -> str:
        if total > 9 * num:
            return ""
        nines = total // 9
        rem = total % 9
        ans = "9" * nines
        if rem:
            ans += str(rem)
        return ans.ljust(num, "0")   