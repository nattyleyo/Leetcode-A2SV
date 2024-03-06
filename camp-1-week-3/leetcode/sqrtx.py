class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if mid**2 > x:
                high = mid - 1
            elif mid**2 < x:
                ans = mid
                low = mid + 1
            else:
                return mid
        return ans

