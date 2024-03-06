class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0
        def haveCapacity(mid):
            curSum = 0
            day = 1
            for i in range(len(weights)):
                curSum += weights[i]
                if curSum > mid:
                    curSum = weights[i]
                    day += 1
            # print(curSum)
            return (day > days)
        while low<=high:
            mid = (low+high)//2
            if haveCapacity(mid):
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans