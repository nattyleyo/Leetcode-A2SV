class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic=defaultdict(int)
        dic[0]+=1
        ans=0
        pref=0
        for i in range(len(nums)):
            pref+=nums[i]
            if pref-goal in dic:
                ans+=dic[pref-goal]
            dic[pref]+=1
        return ans


#0  0   0   0   0
#0  0   0   0   0
#               ^              
# k=0
#ans=15
#0:5,
# 0

