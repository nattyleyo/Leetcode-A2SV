# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        # print(n)
        cur = head
        base , extra = n//k , n%k 
        print(base)
        for i in range(k):
            res.append(cur)
            for j in range( base -1 + (1 if extra else 0)):
                if not cur:
                    break
                cur = cur.next
            extra -= (1 if extra > 0 else 0)
            if cur:
                cur.next , cur = None , cur.next 

        # print(res)
        return res
