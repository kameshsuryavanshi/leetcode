class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str,
                       queries: list[str]) -> list[bool]:

        # ---------- 1) adjacency ----------
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = (n).bit_length()
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n          # 1-based Euler index
        tout = [0] * n
        base = [0] * n         # root->x xor mask, static part

        # ---------- 2) iterative DFS: fill tin/tout/depth/up[0]/base ----------
        timer = 0
        stack = [(0, -1, 0)]   # (node, parent, state) state 0=enter 1=exit
        while stack:
            x, p, st = stack.pop()
            if st == 0:
                timer += 1
                tin[x] = timer
                up[0][x] = p
                base[x] = (base[p] if p != -1 else 0) ^ (1 << (ord(s[x]) - 97))
                stack.append((x, p, 1))
                for y in g[x]:
                    if y != p:
                        depth[y] = depth[x] + 1
                        stack.append((y, x, 0))
            else:
                tout[x] = timer

        for k in range(1, LOG):
            prev, cur_arr = up[k - 1], up[k]
            for v in range(n):
                a = prev[v]
                cur_arr[v] = prev[a] if a != -1 else -1

        # ---------- 3) Fenwick over XOR ----------
        size = n + 2
        bit = [0] * (size + 1)

        def add(i: int, d: int) -> None:      
            while i <= size:
                bit[i] ^= d
                i += i & -i

        def pref(i: int) -> int:              
            s_val = 0
            while i > 0:
                s_val ^= bit[i]
                i -= i & -i
            return s_val

        def range_xor(l: int, r: int, d: int) -> None:
            add(l, d)
            add(r + 1, d)

        def path_mask(x: int) -> int:         # current P(x)
            return base[x] ^ pref(tin[x])

        # ---------- 4) LCA via binary lifting ----------
        def lca(u: int, v: int) -> int:       
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # ---------- 5) process queries ----------
        ans: list[bool] = []
        cur = [1 << (ord(c) - 97) for c in s]

        for q in queries:
            t = q.split()
            if t[0] == "update":
                u, ch = int(t[1]), t[2]
                new = 1 << (ord(ch) - 97)
                delta = cur[u] ^ new
                if delta:
                    cur[u] = new
                    range_xor(tin[u], tout[u], delta)   # subtree flip
            else:
                u, v = int(t[1]), int(t[2])
                w = lca(u, v)
                m = path_mask(u) ^ path_mask(v) ^ cur[w]
                ans.append(m & (m - 1) == 0)

        return ans