class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find_bit_recursive(level: int, position: int) -> int:
            if position == 1:
                return 0
            
            if (position & (position - 1)) == 0:
                return 1
            
            string_length = 1 << level
            
            if position * 2 < string_length - 1:
                return find_bit_recursive(level - 1, position)
            
            mirrored_position = string_length - position
            return find_bit_recursive(level - 1, mirrored_position) ^ 1
        
        return str(find_bit_recursive(n, k))