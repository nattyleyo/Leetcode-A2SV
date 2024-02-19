class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * (n)
        suff = [0] * (n)
        pref[0] = nums[0]                                                                                                                    
        suff[-1] = nums[-1]
        total = sum(nums)
        for i in range(n):
            pref[i] = pref[i-1] + nums[i]
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] + nums[i]
        for i in range(n):
            # res[i] = nums[i]*(i) - pref[i] + suff[i] - nums[i]*(n-i-1) -- this simplified formula for 1-indexed
            res[i] = (nums[i]*(i+1)) - pref[i]
            res[i] += (suff[i] - (nums[i]*(n-i)))            
        return res
#2 3 5
#8 5 0