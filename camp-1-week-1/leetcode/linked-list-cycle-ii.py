# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow  = slow.next
            fast  = fast.next.next
            if slow == fast :
                temp = head
                while slow != temp:
                    slow = slow.next
                    temp = temp.next
                return slow
        return None