from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(float(l) * l for _, _, l in squares)
        target = total_area / 2.0
        
        # Define boundaries based on the actual reach of the squares
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        def get_area_below(y_line):
            area = 0.0
            for _, y_start, l in squares:
                if y_line <= y_start:
                    continue
                if y_line >= y_start + l:
                    area += float(l) * l
                else:
                    # Only the portion of the square below y_line
                    area += float(l) * (y_line - y_start)
            return area

        # Use 100 iterations for maximum floating point precision
        for _ in range(100):
            mid = (low + high) / 2
            # Checking area below vs target (or area above, both work)
            if get_area_below(mid) < target:
                low = mid
            else:
                high = mid
                
        return low
        