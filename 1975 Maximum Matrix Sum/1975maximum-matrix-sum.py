class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0 
        min_a = float('inf')
        n_count = 0
        for r in matrix:
            for v in r:
                total += abs(v)
                min_a = min(min_a,abs(v))
                if v < 0 :
                    n_count += 1
        if n_count % 2 == 1:
            return total - 2* min_a
        else :
            return total