class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2 == 0:
            even = n //2
        else:
            even = 1+ n //2
        odd = n //2
        # else:
        #     n = 1+ n//2
        def myFunc5(base,n):
            if n==1:
                return base
            if n == 0:
                return 1
            if n%2 == 0:
                num = myFunc5(base,n//2)
                return (num**2)%((10**9)+7)
            else:
                num = myFunc5(base,n//2)
                return ((num**2)*base)%((10**9)+7)
        # def myFunc4(n):
        #     if n==1:
        #         return 4
            
        #     if n%2 == 0:
        #         num = myFunc4(n//2)
        #         return (num**2)%((10**9)+7)
        #     else:
        #         num = myFunc4(n//2)
        #         return ((num**2)*4)%((10**9)+7)
        return ((myFunc5(4,odd) if myFunc5(4,odd) else 1)* myFunc5(5,even))%((10**9)+7)

                

           


        