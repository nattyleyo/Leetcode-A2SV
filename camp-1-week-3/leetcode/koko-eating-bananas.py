class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans =0
        def decider(mid):
            eat = 0
            hour = 0
            for i in range(len(piles)):
                hour += ceil( piles[i]/mid )
            return hour <= h
        while low <= high:
            mid = (low + high)//2
            if decider(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans