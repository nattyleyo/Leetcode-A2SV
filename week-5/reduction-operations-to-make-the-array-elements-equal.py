class Solution:
  def reductionOperations(self, nums: List[int]) -> int:
    ans = 0
    n=len(nums)
    nums.sort()
    for i in range(n - 1, 0, -1):
      if nums[i] != nums[i - 1]:
        ans += n - i
    return ans
    #1,3,5