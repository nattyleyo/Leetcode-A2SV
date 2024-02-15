class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        j=0
        k=0
        ans=float('inf')
        res=0
        nums.sort()
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                threeSum=nums[i]+nums[j]+nums[k]
                if threeSum == target:
                    return target
                elif abs(threeSum - target) < abs(ans):
                    ans= threeSum - target
                    res= threeSum
                if threeSum < target:
                    j+=1
                else:
                    k-=1
        return res


