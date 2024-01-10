class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        my_max=float('-inf')
        tempSum=sum(nums[:k])
        left=0
        right=k-1
        while right<len(nums):
            my_max=max(my_max,tempSum/k)
            right+=1
            if right<len(nums):
                tempSum+=nums[right]
                tempSum-=nums[left]
                left+=1
        return my_max

        