class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        maxCan=0
        res=[]
        for i in range(n):
            maxCan=candies[i]+extraCandies
            if maxCan>=max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
                