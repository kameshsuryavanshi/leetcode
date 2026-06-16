class Solution:
    def processStr(self, s: str) -> str:
        result = []
        
        for char in s:
            if char == '*':
                if result:  # Only pop if result is not empty
                    result.pop()
            elif char == '#':
                result = result + result  # Duplicate the list
            elif char == '%':
                result = result[::-1]  # Reverse the list
            else:
                result.append(char)  # Append lowercase letter
        
        return ''.join(result)