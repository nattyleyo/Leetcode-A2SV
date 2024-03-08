class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        last = float('-inf')
        for i in range( n-1,-1,-1):
            if nums[i] < last:
                return True
            while stack and nums[i] > stack[-1]:
                last = stack.pop()
            stack.append(nums[i])
        return False
        