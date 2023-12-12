class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        maxSq = 0
        for num in nums:
            if num - 1 not in my_set:
                temp = 1
                while num + 1 in my_set:
                    temp += 1
                    num += 1
                maxSq = max(maxSq, temp)
        return maxSq

        