# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from types import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def fillNode(self, nums: List[int], node: TreeNode) -> TreeNode:
        l = len(nums)

        if not l:
            return None

        med = l // 2

        left = nums[:med]
        right = nums[med + 1:]

        node.val = nums[med]
        node.left = self.fillNode(left, TreeNode())
        node.right = self.fillNode(right, TreeNode())

        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.fillNode(nums, TreeNode())



#############################

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if r < l:
                return None
            if r == l:
                return TreeNode(nums[r])
            mid = (l + r)//2
            node = TreeNode(nums[mid])
            node.left = helper(l, mid-1)
            node.right = helper(mid+1, r)
            return node
        return helper(0, len(nums) - 1)
