class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        sign = 1
        if not s:
            return 0
        
        if s[0] == "-":
            sign= -1
            s=s[1:]
        elif s[0] == "+":
            sign = 1
            s=s[1:]

        result = 0
        for Char in s:
            if Char.isdigit() :
                 result = result * 10 + int(Char)
            else:
                 break
            
        result *= sign

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result