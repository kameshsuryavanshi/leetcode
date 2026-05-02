class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length == 0:
            return 0
        
        totalsum = sum(A)
        res = 0
        for idx in range(length):
            res += idx * A[idx]
        maxval = res
        
        for idx in range(length):
            # res -= totalsum
            res += length * A[idx] - totalsum
            maxval = max(maxval,res)
        return maxval