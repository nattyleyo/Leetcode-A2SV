class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        left=0
        right=n-1
        count=0
        print(nums)
        while left<right:
            tempSum=nums[left]+nums[right]
            if tempSum < target:
                count+=right-left
                left+=1
            else:
                right-=1
        return count



#-7 -6 -2 -1 2 3 5
#       ^  ^    
#=10
