# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #approch-1 using set
        # my_set=set()
        # current=head
        # while current:
        #     my_set.add(current)
        #     current=current.next
        #     if current in my_set:
        #         return True
        # return False
        
        #approch-2 using pointer
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False