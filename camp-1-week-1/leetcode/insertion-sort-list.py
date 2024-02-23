# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current.next is not None:
            if current.next.val < current.val:
                prev = dummy
                while prev.next is not None and prev.next.val < current.next.val:
                    prev = prev.next
                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                current = current.next
        return dummy.next