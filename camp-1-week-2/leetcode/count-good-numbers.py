class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2 == 0:
            even = n //2
        else:
            even = 1+ n //2
        odd = n //2
        def powerFunc(base,n):
            if n==1:
                return base
            if n == 0:
                return 1
            if n%2 == 0:
                num = powerFunc(base,n//2)
                return (num**2)%((10**9)+7)
            else:
                num = powerFunc(base,n//2)
                return ((num**2)*base)%((10**9)+7)
 
        return ((powerFunc(4,odd) if powerFunc(4,odd) else 1)* powerFunc(5,even))%((10**9)+7)

                

           


        