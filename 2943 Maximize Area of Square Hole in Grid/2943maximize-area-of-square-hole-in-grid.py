from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_gap(bars):
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    max_consecutive = max(max_consecutive, current_consecutive)
                    current_consecutive = 1 
            max_consecutive = max(max_consecutive, current_consecutive)
            
            return max_consecutive + 1

        max_h_gap = get_max_gap(hBars)
        max_v_gap = get_max_gap(vBars)

        side = min(max_h_gap, max_v_gap)

        return side * side