class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largeSum= nums[0]
        pref=0
        for i in range(len(nums)):
            pref += nums[i]
            largeSum = max(largeSum,pref)
            if pref < 0:
                pref = 0
        return largeSum
#-2  1   -3  4 -1   2  1 -5  4
# 0  1    0  4  3   5  6
