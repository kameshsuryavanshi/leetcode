class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(map(str, digits))
        plus_one = str(int(s) + 1)
        return [int(char) for char in plus_one]