class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0
        def helper(mid):
            divSum = 0
            for i in range(len(nums)):
                divSum += ceil(nums[i]/mid)
            return (divSum > threshold)

        while low <= high:
            mid = (low + high)//2
            if helper(mid):
                low = mid + 1
            else:
                ans = mid
                high = mid -1
        return ans
