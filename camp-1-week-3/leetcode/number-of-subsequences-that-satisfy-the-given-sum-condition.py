class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        mod = 10**9 + 7
        for i in range(len(nums)):
            j = bisect_right( nums , target-nums[i])
            if i >= j:
                break
            ans += pow(2,j-i-1,mod)
        return ans % mod
        
        
        
        
        
        