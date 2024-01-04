class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if len(s)==0:
            return True

        s=''.join([char for char in s if char.isalnum()])
        left=0
        right=len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

        

#raceacar
#   ^ ^