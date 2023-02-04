# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def addHead(self, node, val):
        curr_node = ListNode(val)

        curr_node.next = node

        return curr_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        reversed = ListNode(head.val)
        t = head.next
        while (t):
            reversed = self.addHead(reversed, t.val)
            t = t.next

        return reversed
