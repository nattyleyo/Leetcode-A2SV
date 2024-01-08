class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c=Counter(costs)
        ans=0
        re,tt=0,0
        for i in range(min(costs),max(costs)+1):
            for j in range(c[i]):
                print(ans)
                if ans<=coins:
                    maxa=ans
                    tt=re
                ans+=i
                re+=1
            if ans<=coins:
                maxa=ans
                tt=re
        if maxa<=coins:
            return tt
        return 0