import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        
        # L and R act as a Doubly Linked List to keep track of neighbors
        L = [i - 1 for i in range(n)]
        R = [i + 1 for i in range(n)]
        R[-1] = -1
        
        # Track how many adjacent elements are not sorted
        inversions = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                inversions += 1
        
        # Min-heap stores (sum, index). 
        # Python's heapq will pick the smallest index for tied sums.
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nums[i] + nums[i+1], i))
            
        ops = 0
        deleted = [False] * n
        
        while inversions > 0:
            s, i = heapq.heappop(pq)
            
            # Validation: i must not be deleted and its current right neighbor 
            # must result in the sum we popped (Lazy Deletion check).
            j = R[i]
            if deleted[i] or j == -1 or (nums[i] + nums[j] != s):
                continue
            
            # 1. Update Inversions: Remove current pair and affected neighbors
            if nums[i] > nums[j]: inversions -= 1
            
            prev = L[i]
            if prev != -1:
                if nums[prev] > nums[i]: inversions -= 1
                
            nxt = R[j]
            if nxt != -1:
                if nums[j] > nums[nxt]: inversions -= 1
            
            # 2. Merge j into i
            nums[i] += nums[j]
            deleted[j] = True
            ops += 1
            
            # 3. Re-link the Doubly Linked List
            R[i] = nxt
            if nxt != -1:
                L[nxt] = i
            
            # 4. Add back Inversions for updated values
            if prev != -1:
                if nums[prev] > nums[i]: inversions += 1
                # Push new neighbor sum
                heapq.heappush(pq, (nums[prev] + nums[i], prev))
                
            if nxt != -1:
                if nums[i] > nums[nxt]: inversions += 1
                # Push new neighbor sum
                heapq.heappush(pq, (nums[i] + nums[nxt], i))
                
        return ops