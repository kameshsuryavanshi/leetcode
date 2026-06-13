from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            word_weight = 0
            for char in word:
                index = ord(char) - ord('a')
                word_weight += weights[index]
            
            mapped_index = word_weight % 26
            mapped_char = chr(ord('z') - mapped_index)
            
            result.append(mapped_char)
        
        return ''.join(result)