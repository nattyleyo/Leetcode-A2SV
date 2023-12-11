class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            if 2*i+1<n:
                freq=nums[2*i]
                val=nums[2*i+1]
                for j in range(freq):
                    res.append(val)
        return res
            
        