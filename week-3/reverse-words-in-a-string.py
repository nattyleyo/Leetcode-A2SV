class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        temp=list(s.split())
        n=len(temp)
        for i in range(-1,-n-1,-1):
            res.append(temp[i])
        return ' '.join(res)