class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in m:
                return [m[y], i]
            m[x] = i