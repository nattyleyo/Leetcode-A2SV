class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        n=len(boxes)
        for i in range(n):
            move=0
            for j in range(n):
                move+=abs(i-j)
                if move<1 or boxes[j]=='0':
                    move-=abs(i-j)
            ans.append(move)
        return ans

