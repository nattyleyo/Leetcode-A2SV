class Solution:
    def canJump(self, nums):
        max_idx = nums[0]

        for i in range(len(nums)):
            if max_idx >= len(nums) - 1:
                return True
            if nums[i] == 0 and max_idx == i:
                return False
            max_idx = max( max_idx, i+nums[i])
        return True
#0,1,2,3,4
#2,3,1,1,4
#  ^
#==2
#==4