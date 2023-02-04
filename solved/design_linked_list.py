# https://leetcode.com/problems/design-linked-list/description/

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        tmp_head = self.head
        while index > 0:
            if not tmp_head:
                break
            tmp_head = tmp_head.next
            index -= 1

        return -1 if not tmp_head else tmp_head.val

    def addAtHead(self, val: int) -> None:
        curr_head = self.head
        self.head = Node(val)
        self.head.next = curr_head

    def addAtTail(self, val: int) -> None:
        last_head = self.head

        if not last_head:
          self.addAtHead(val)
          return

        while (last_head.next):
            last_head = last_head.next

        last_head.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
            return

        tmp_head = self.head
        while tmp_head and index > 1:
            tmp_head = tmp_head.next
            index -= 1

        if tmp_head:
            next_head = tmp_head.next

            curr_node = Node(val)
            curr_node.next = next_head
            tmp_head.next = curr_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next if self.head else None
            return

        prev_head = self.head
        while prev_head and index > 1:
            prev_head = prev_head.next
            index -= 1

        if prev_head:
            next_head = prev_head.next.next if prev_head.next else None

            prev_head.next = next_head

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)



# ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
# [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
# [null,null,-1,null,null,null,null,4,4,4,null,null]