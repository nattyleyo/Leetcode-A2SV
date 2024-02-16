class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count = 0
        total = 0
        odd = 0
        n = len(nums)
        while right < n:
            if nums[right]%2 != 0:
                odd += 1
                count = 0
            if odd == k:
                while left < n and nums[left]%2 == 0:
                    count += 1
                    left += 1
                count += 1
                left += 1
                odd -= 1
            right += 1
            total += count
        return total