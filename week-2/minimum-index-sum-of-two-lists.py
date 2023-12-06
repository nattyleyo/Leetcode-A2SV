class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictn={}
        res=[]*10
        minCom=float('inf')
        for i in range(len(list1)):
            iSum=0
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    iSum=i+j
                    dictn[list1[i]]=iSum
                    break
        for i,j in dictn.items():
            minCom=min(minCom,j)
        for key,val in dictn.items():
            if val==minCom:
                res.append(key)
        return res
            
            
            