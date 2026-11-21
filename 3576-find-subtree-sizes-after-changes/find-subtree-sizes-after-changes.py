
from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(node: int, parent_node: int) -> None:
            subtree_sizes[node] = 1
            char_stack[s[node]].append(node)
            for child in adjacency_list[node]:
                dfs(child, node)
            target_ancestor = parent_node
            if len(char_stack[s[node]]) > 1:
                target_ancestor = char_stack[s[node]][-2]
            if target_ancestor != -1:
                subtree_sizes[target_ancestor] += subtree_sizes[node]
            char_stack[s[node]].pop()

        n = len(s)
        adjacency_list = [[] for _ in range(n)]
        for i in range(1, n):
            adjacency_list[parent[i]].append(i)
        char_stack = defaultdict(list)
        subtree_sizes = [0] * n
        dfs(0, -1)
        return subtree_sizes