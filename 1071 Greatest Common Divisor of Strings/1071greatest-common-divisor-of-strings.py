class Solution(object):
    def gcdOfStrings(self, str1, str2):

        len1, len2 = len(str1), len(str2)

        if str1 + str2 != str2 + str1:
            return ""
        def gcd (a , b) :
            if b==0: 
                return a
            return gcd(b,a%b)

        gcd_len = gcd(len1, len2)

        return str1[:gcd_len]
        