class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m=len(nums)
        res=[]*m
        for i in range(m-n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res