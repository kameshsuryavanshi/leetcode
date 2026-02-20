class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def split(S):
            count = i = 0
            for j, char in enumerate(S):
                count = count + 1 if char == '1' else count - 1
                if count == 0:
                    yield S[i:j+1]
                    i = j + 1
        
        mountains = sorted((("1" + self.makeLargestSpecial(m[1:-1]) + "0") for m in split(s)), reverse=True)
        return ''.join(mountains)