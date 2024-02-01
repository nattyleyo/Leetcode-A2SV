# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        left=head
        right=left.next
        while right:
            if right.val==left.val:
                left.next=None
            else:
                left.next=right
                left=left.next
            right=right.next
        return head

#1  1  2
#^
#      ^     
        