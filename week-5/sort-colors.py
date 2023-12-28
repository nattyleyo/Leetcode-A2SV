class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        minIdx=0
        for i in range(n):
            for j in range(i,n):
                if nums[i]>=nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]   
        return nums

        