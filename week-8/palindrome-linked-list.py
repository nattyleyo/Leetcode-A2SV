# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        cur=slow
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        # print(head)
        # print(prev)
        while prev and head:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True