class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1: 
                return -1
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1: 
                return -1
            
            # If current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Otherwise, return the height of the current node
            return max(left_height, right_height) + 1
            
        return check_height(root) != -1