# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        a=list1
        b=list2
        while a and b:
            if a.val <= b.val:
                cur.next=a
                a=a.next
            else:
                cur.next=b
                b=b.next
            cur=cur.next
        if a is None:
            cur.next=b
        else: 
            cur.next = a
        return dummy.next


#1 1  2 3 4
#1  2   4
#           ^
#1  3   4      
#       ^