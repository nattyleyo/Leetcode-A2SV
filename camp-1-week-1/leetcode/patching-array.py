class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        max_ = 0
        r = 0
        while max_ < n:
            if r < len(nums) and nums[r] <= max_ + 1:
                max_ += nums[r]
                r += 1
            else:
                add = max_ + 1
                max_ += add
                res += 1
        return res
                

#1 2 5 6 20
#        ^
#max=57
#1~57
#n=50
#[4,19]