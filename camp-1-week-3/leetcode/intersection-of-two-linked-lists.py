# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        q = headB
        lenA = 0
        lenB = 0
        ans = 0
        while p:
            lenA += 1
            p = p.next
        while q:
            lenB += 1
            q = q.next
        p = headA
        q = headB
        for i in range(abs(lenA-lenB)):
            if lenA > lenB:
                p = p.next
            else:
                q = q.next
        while q and p:
            if q == p:
                break
            q = q.next
            p = p.next

        return q