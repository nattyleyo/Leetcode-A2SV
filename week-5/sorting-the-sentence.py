class Solution:
    def sortSentence(self, s: str) -> str:
        di=defaultdict(str)
        tempArr=list(s.split())
        res=[]
        for i in range(len(tempArr)):
            tempStr=tempArr[i]
            val=tempStr[:-1]
            key=int(tempStr[-1])
            di[key]=val
        print(di)
        mykeys=list(di.keys())
        mykeys.sort()
        for key in mykeys:
            res.append(di[key])
        return ' '.join(res)
        