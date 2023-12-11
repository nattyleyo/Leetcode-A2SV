class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n=len(s)
        m=len(spaces)
        start=0
        res=[]
        for i in range(m):
            res.append(s[start:spaces[i]])
            start=spaces[i]
        res.append(s[spaces[m-1]:n])
        return ' '.join(res)


        