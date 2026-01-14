class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # 1. Collect all unique x-coordinates for coordinate compression
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        sorted_xs = sorted(xs)
        x_map = {val: i for i, val in enumerate(sorted_xs)}
        n_x = len(sorted_xs)

        # 2. Segment Tree to manage union of x-intervals
        # count[i] tracks how many squares cover the segment between sorted_xs[i] and sorted_xs[i+1]
        # length[i] tracks the total covered width in the subtree
        count = [0] * (4 * n_x)
        length = [0.0] * (4 * n_x)

        def update(v, tl, tr, l, r, add):
            if l >= r:
                return
            if l == tl and r == tr:
                count[v] += add
            else:
                tm = (tl + tr) // 2
                update(2 * v, tl, tm, l, min(r, tm), add)
                update(2 * v + 1, tm, tr, max(l, tm), r, add)
            
            if count[v] > 0:
                length[v] = sorted_xs[tr] - sorted_xs[tl]
            else:
                if tr - tl > 1:
                    length[v] = length[2 * v] + length[2 * v + 1]
                else:
                    length[v] = 0.0

        # 3. Create vertical events (y, type, x_start, x_end)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        # 4. First pass: Calculate total area and store slices
        total_area = 0.0
        slices = [] # (y_start, y_end, covered_x_width)
        
        for i in range(len(events) - 1):
            y, type_change, x1, x2 = events[i]
            update(1, 0, n_x - 1, x_map[x1], x_map[x2], type_change)
            
            next_y = events[i+1][0]
            if next_y > y:
                width = length[1]
                area_slice = width * (next_y - y)
                total_area += area_slice
                slices.append((y, next_y, width))

        # 5. Second pass: Find the y-level that splits the total area
        half_target = total_area / 2.0
        current_area = 0.0
        for y_start, y_end, width in slices:
            slice_area = width * (y_end - y_start)
            if current_area + slice_area >= half_target:
                # Solve for the exact y within this slice: 
                # current_area + width * (y_ans - y_start) = half_target
                return y_start + (half_target - current_area) / width
            current_area += slice_area
            
        return events[-1][0]