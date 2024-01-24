# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow=0
        # fast=0
        my_set=set()
        current=head
        while current:
            my_set.add(current)
            current=current.next
            if current in my_set:
                return True
        return False
        