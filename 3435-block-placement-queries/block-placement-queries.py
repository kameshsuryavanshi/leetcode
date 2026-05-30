from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # Determine the maximum coordinate boundary needed
        max_x = min(50000, 3 * len(queries)) + 1
        
        # Segment tree to store maximum gaps
        seg_tree = SegmentTree(max_x)
        
        # SortedList to maintain active obstacle positions
        obstacles = SortedList([0, max_x])
        
        # Initially, the only gap is between 0 and max_x
        seg_tree.update(1, 0, max_x, max_x, max_x)
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find where x fits among existing obstacles
                idx = obstacles.bisect_left(x)
                left_obs = obstacles[idx - 1]
                right_obs = obstacles[idx]
                
                # Insert x into obstacles
                obstacles.add(x)
                
                # Update distances in the segment tree
                seg_tree.update(1, 0, max_x, x, x - left_obs)
                seg_tree.update(1, 0, max_x, right_obs, right_obs - x)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                
                # Find the obstacle immediately to the left of x
                idx = obstacles.bisect_right(x)
                left_obs = obstacles[idx - 1]
                
                # 1. Get max gap completely inside [0, left_obs]
                max_gap_built = seg_tree.query(1, 0, max_x, 0, left_obs)
                
                # 2. Check the remaining partial gap between left_obs and x
                partial_gap = x - left_obs
                
                # If either space is big enough, append True
                if max(max_gap_built, partial_gap) >= sz:
                    results.append(True)
                else:
                    results.append(False)
                    
        return results