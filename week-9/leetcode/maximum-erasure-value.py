class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        curr_sum = 0
        max_sum = 0
        left = 0
        right = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            curr_sum += nums[right]
            seen.add(nums[right])
            max_sum = max(max_sum, curr_sum)
        return max_sum