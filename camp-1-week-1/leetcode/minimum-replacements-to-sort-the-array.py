class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        last = 0
        lastIdx = n-2
        while lastIdx >= 0:
            last = nums[lastIdx + 1]
            if nums[lastIdx] > last:
                cur = math.ceil( nums[lastIdx]/last)
                count += cur-1
                nums[lastIdx] = nums[lastIdx]//cur
            lastIdx -= 1
            # print(cur)
        return count

#[12,9,7,6,17,19,21]
#      ^
#cur=12  1 6
#last=6
#count=2