class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_d={}
        n=len(nums)
        for i in range(n+1):
            num_d[i]=0
        for i in range(n):
           num_d[nums[i]]=1
        for key in num_d:
            if num_d[key]==0:
                return key



        