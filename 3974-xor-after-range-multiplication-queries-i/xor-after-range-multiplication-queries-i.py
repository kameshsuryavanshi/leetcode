class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 1_000_000_007
        
        # Process each query
        for query in queries:
            left, right, step, value = query
            
            # Update elements at indices: left, left+step, left+2*step, ...
            for index in range(left, right + 1, step):
                nums[index] = (nums[index] * value) % MOD
        
        # Compute XOR of all elements
        answer = 0
        for num in nums:
            answer ^= num
        
        return answer