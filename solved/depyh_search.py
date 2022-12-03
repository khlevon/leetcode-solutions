# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_depths = [1]

        def explore_node(node: TreeNode, depth: int):
            if node is None:
                max_depths.append(depth - 1)
                return

            explore_node(node.left, depth + 1)
            explore_node(node.right, depth + 1)

        explore_node(root, 1)

        return max(max_depths)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, root):
        if root is None:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        return max(left, right) + 1
