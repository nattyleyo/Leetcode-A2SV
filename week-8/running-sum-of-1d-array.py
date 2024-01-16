class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runingSum=[0]*len(nums)
        runingSum[0]=nums[0]
        print(runingSum[0])
        for i in range(1,len(nums)):
            runingSum[i]=runingSum[i-1]+nums[i]
        return runingSum
        # return []