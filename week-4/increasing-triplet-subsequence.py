class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=max(nums)
        j=max(nums)
        for k in range(len(nums)):
            if nums[k]<=i:
                i=nums[k]
            elif nums[k]<=j:
                j=nums[k]
            else:
                return True
        return False
