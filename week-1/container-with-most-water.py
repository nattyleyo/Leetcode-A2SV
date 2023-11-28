class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxW = 0
        left, right = 0, len(height) - 1

        while left < right:
            h_left, h_right = height[left], height[right]
            width = right - left
            current = min(h_left, h_right) * width

            maxW = max(maxW, current)

            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return maxW