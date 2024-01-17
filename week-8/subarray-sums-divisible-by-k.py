class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]+=1
        ans=0
        prefix=0
        for i in nums:
            prefix+=i
            if (prefix % k in dic):
                ans+=dic[prefix % k]
            dic[prefix % k]+=1
        return ans
