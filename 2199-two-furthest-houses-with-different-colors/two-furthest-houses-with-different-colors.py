class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        length = len(colors)
        for index, color in enumerate(colors):
            if color != colors[0]:
                distance = max(distance, index)
            if color != colors[length-1]:
                distance = max(distance, length - 1 - index)
        return distance