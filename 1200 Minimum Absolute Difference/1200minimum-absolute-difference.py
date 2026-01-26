class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        min_diff = float('inf')
        res = []
        
        # Step 2: Single pass to find min_diff and collect pairs
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            
            if current_diff < min_diff:
                # Found a new smaller difference, reset the list
                min_diff = current_diff
                res = [[arr[i], arr[i+1]]]
            elif current_diff == min_diff:
                # Found another pair with the same minimum difference
                res.append([arr[i], arr[i+1]])
                
        return res