class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        last = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans += (i - last)
                last +=1
        return ans
#101
# ^