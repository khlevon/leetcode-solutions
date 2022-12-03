# Definition for a binary tree node.
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.deps(root)

    def deps(self, node: Optional[TreeNode]):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        left = self.deps(node.left)
        right = self.deps(node.right)

        if left == 0:
            return right + 1

        if right == 0:
            return left + 1

        return min(left, right) + 1


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))