class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n=len(fronts)
        p=0
        inval=set()
        minVal=float('inf')
        res=[]
        flag=False
        for i in range(n):
            if fronts[i]==backs[i]:
                inval.add(fronts[i])
        while p<n:
            if fronts[p] not in inval:
                minVal=min(minVal,fronts[p])
            if backs[p] not in inval :
                minVal=min(minVal,backs[p])
            p+=1
        if minVal==float('inf'):
            return 0
        else:
            return minVal

                

        
        
