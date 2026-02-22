class Solution:
    def binaryGap(self, n: int) -> int:
        max_distance = 0
        previous_one_position = float('inf')
        current_position = 0
        
        while n > 0:
            if n & 1:
                max_distance = max(max_distance, current_position - previous_one_position)
                previous_one_position = current_position
            
            current_position += 1
            n >>= 1
        
        return max_distance