class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_z = [c for c in str(n) if c != '0']
        if not non_z :
            return 0
        x = int(''.join(non_z))
        digit_sum = sum(int(d) for d in str(x))
        return x * digit_sum
        
