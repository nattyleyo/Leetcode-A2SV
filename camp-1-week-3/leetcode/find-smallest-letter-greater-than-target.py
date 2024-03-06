class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n - 1
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if letters[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return letters[ans]