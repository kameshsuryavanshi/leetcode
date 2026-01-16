class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        hFences.sort()
        vFences.sort()
        
        def get_all_gaps(fences):
            gaps = set()
            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    
                    gaps.add(fences[j] - fences[i])
            return gaps
        
        h_gaps = get_all_gaps(hFences)
        v_gaps = get_all_gaps(vFences)
        
        common_gaps = h_gaps.intersection(v_gaps)
        
        if not common_gaps:
            return -1
        
        max_side = max(common_gaps)
        return (max_side * max_side) % MOD