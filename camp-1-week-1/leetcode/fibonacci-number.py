class Solution:
    @cache
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        return n if n<2 else self.fib(n-1) + self.fib(n-2)