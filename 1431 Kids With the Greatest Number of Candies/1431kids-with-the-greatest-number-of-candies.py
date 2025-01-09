class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_c = max(candies) 
        result = []
        for candy in candies :
            result.append(candy + extraCandies >= max_c)
        
        return result 