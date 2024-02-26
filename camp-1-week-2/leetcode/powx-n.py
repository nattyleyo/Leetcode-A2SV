class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        def powerFunc(base,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n%2 == 0:
                num = powerFunc(base,n//2)
                return num*num
            else:
                num = powerFunc(base,n//2)
                return (num**2)*base
        res = powerFunc(base,abs(n))
        return res if n>= 0 else 1/res