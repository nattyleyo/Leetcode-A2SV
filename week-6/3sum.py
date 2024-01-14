class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)-2):
            if  (nums[i]>0 ):return ans
            l,r=i+1,len(nums)-1
            t=nums[i]+nums[l]+nums[r]
            while(  r>l):
                if t>0:
                    r-=1
                elif t<0:
                    l+=1
                else:
                    ans.add((nums[i],nums[l],nums[r]))
                    r-=1
                    l+=1
                t=nums[i]+nums[l]+nums[r]
        return ans