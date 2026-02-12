class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            counts = {}
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                frequencies = list(counts.values())
                
                if len(set(frequencies)) == 1:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len