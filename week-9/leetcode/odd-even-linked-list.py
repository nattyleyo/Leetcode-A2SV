# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=1
        dic={}
        if head is None:
            return head
        p=head
        while p:
            if p.next is None:
                tail=p
            dic[p]=count
            count+=1
            p=p.next
        if len(dic)==2:
            return head
        right=head
        count=1
        my_max=max(dic.values())
        while right and dic[right]!=max(dic.values()):
            q=right.next
            right.next=q.next
            q.next=None
            tail.next=q
            tail=tail.next 
            if dic[right]== my_max-1 and dic[right]%2!=0:
                break
            right=right.next

        # print(tail)
        return head
        
        
# 1   2   3   4   5
#                 ^ 
# curOdd->5
# curEven->4
# p->1->3->5
# q->2->4