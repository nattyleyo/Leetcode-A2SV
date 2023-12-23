class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_zeros = 0
        right_ones = nums.count(1)
        max_score = 0
        res = []

        for i in range(n + 1):
            score = left_zeros + right_ones
            if score > max_score:
                max_score = score
                res = [i]  
            elif score == max_score:
                res.append(i)
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1
        return res
