# https://leetcode.com/problems/symmetric-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def compare(self, p: Optional[TreeNode], q: Optional[TreeNode]):

        if not p or not q:
            return not p and not q

        plv = p.left.val if p.left else None
        prv = p.right.val if p.right else None
        qlv = q.left.val if q.left else None
        qrv = q.right.val if q.right else None

        if not (plv == qrv and prv == qlv):
            return False

        return self.compare(p=p.left, q=q.right) and self.compare(p=q.left, q=p.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = root.left
        right = root.right

        if not left or not right:
            return not left and not right

        if left.val != right.val:
            return False

        if not self.compare(left, right):
            return False

        return True

# [1,2,2,3,4,4,3]
# [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
# [9,-42,-42,null,76,76,null,null,13,null,13]

# None None
# first True

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def isSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
#             if not (left and right):
#                 return left == right

#             return left.val == right.val and isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)

#         return isSymmetric(root.left, root.right)
