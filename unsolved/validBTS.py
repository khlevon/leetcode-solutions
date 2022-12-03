# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
from typing import Optional

# todo: not solved


class TreeNode:
    def __init__(self, val=0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.nodes_stack = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.nodes_stack.append(root.val)

        if not root.left and not root.right:
            self.nodes_stack.pop()
            return True

        if (root.left and root.left.val) >= root.val or (root.right and root.right.val) <= root.val:
            self.nodes_stack.pop()
            return False

        for i in self.nodes_stack[:-1]:
            if i >= root.val:
                self.nodes_stack.pop()
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
