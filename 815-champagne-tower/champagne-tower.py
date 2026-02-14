class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        row_data = [poured]
        
        for r in range(query_row):
            next_row = [0.0] * (len(row_data) + 1)
            
            for c in range(len(row_data)):
                excess = (row_data[c] - 1.0) / 2.0
                
                if excess > 0:
                    next_row[c] += excess
                    next_row[c + 1] += excess
            
            row_data = next_row
            
        return min(1.0, row_data[query_glass])