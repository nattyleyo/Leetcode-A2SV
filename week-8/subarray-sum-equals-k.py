class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dic=defaultdict(int)
        dic[0]+=1
        ans=0
        prefix=0
        for i in nums:
            prefix+=i
            if(prefix-k in dic):
                ans+=dic[prefix-k]
            dic[prefix]+=1
        return ans
# 0:2,1:1
# 1 2 3