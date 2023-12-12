class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        di=defaultdict(lambda:1)
        n=len(arr)
        for i in range(n):
            key=arr[i]
            if key in di:
                di[key]+=1
            else:
                di[key]+=0
        maxApp=max(di.values())
        for key,val in di.items():
            if maxApp==val and maxApp/n>0.25:
                return key
        return -1

        