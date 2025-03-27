class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        if n == 1:
            return s

        length = 0
        longest = ""
        longest_len = 0

        def expand_around_center(left, right, current_longest, current_longest_len):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > current_longest_len:
                current_longest_len = length
                current_longest = s[left + 1:right]
            return current_longest, current_longest_len

        for i in range(n):
            longest, longest_len = expand_around_center(i, i, longest, longest_len)
            longest, longest_len = expand_around_center(i, i + 1, longest, longest_len)

        return longest