class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=str(x)
        return p==p[::-1]