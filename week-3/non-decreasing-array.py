class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = False
        if nums == sorted(nums):
            return True
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if flag:
                    return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                flag = True
        return True