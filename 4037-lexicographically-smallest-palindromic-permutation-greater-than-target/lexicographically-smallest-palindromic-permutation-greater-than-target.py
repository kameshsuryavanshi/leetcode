from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check palindrome validity (at most one odd frequency)
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {ch: count // 2 for ch, count in counts.items()}
        half_len = n // 2
        
        candidates = []
        
        # Helper to construct full palindrome from left half
        def make_pal(left_half: list[str]) -> str:
            lh = "".join(left_half)
            return lh + mid_char + lh[::-1]

        # --- Option 1: Match a prefix of target[:half_len] of length i ---
        # Then pick a character > target[i] at position i
        
        prefix = []
        curr_counts = half_counts.copy()
        
        for i in range(half_len + 1):
            if i > 0:
                prev_char = target[i - 1]
                if curr_counts.get(prev_char, 0) == 0:
                    break  # Cannot match target's prefix further
                curr_counts[prev_char] -= 1
                prefix.append(prev_char)
            
            if i == half_len:
                # Option 2: Full left half matches target[:half_len]
                pal = make_pal(prefix)
                if pal > target:
                    candidates.append(pal)
                break
            
            # Try to place a character > target[i] at index i
            target_char = target[i]
            for ch in sorted(curr_counts.keys()):
                if ch > target_char and curr_counts[ch] > 0:
                    # Place ch at index i, then fill rest greedily with smallest available
                    temp_counts = curr_counts.copy()
                    temp_counts[ch] -= 1
                    
                    suffix = []
                    for c in sorted(temp_counts.keys()):
                        suffix.extend([c] * temp_counts[c])
                    
                    left_half = prefix + [ch] + suffix
                    pal = make_pal(left_half)
                    if pal > target:
                        candidates.append(pal)
                        break  # Found the smallest choice for this prefix length
                        
        if not candidates:
            return ""
            
        return min(candidates)