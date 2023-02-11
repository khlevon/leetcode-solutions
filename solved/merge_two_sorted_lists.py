# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        output = ListNode()

        head = output

        # curr = output

        if not list1:
            return list2
        if not list2:
            return list1

        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    output.val = list2.val
                    if list2.next:
                        output.next = ListNode()
                        output = output.next
                    list2 = list2.next
                else:
                    output.val = list1.val
                    if list1.next:
                        output.next = ListNode()
                        output = output.next

                    list1 = list1.next
            elif list1:
                output.next = list1
                return head
            elif list2:
                output.next = list2
                return head

        return head
