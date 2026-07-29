from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10 ** 6 + 1

        freq = Counter(s)

        mid = ""
        half = [0] * 26
        m = 0

        for ch in sorted(freq):
            if freq[ch] & 1:
                mid = ch
            idx = ord(ch) - ord('a')
            half[idx] = freq[ch] // 2
            m += half[idx]

        # Count distinct permutations of the remaining multiset.
        def countWays(cnt):
            total = sum(cnt)
            ans = 1
            rem = total

            for c in cnt:
                if c:
                    ans *= comb(rem, c)
                    if ans > LIMIT:
                        return LIMIT
                    rem -= c

            return ans

        if countWays(half) < k:
            return ""

        left = []

        while m > 0:

            for i in range(26):

                if half[i] == 0:
                    continue

                half[i] -= 1

                ways = countWays(half)

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    m -= 1
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)

        return left + mid + left[::-1]