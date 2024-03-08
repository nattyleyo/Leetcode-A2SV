class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def helper(s):
            my_set = set(s)
            if len(s) < 2:
                return ''
            for i in range(len(s)):
                if s[i].upper() in my_set and s[i].lower() in my_set:
                    continue
                left = helper(s[:i])
                right = helper(s[i+1:])
                return left if len(left) >= len(right) else right
            return s
        return  helper(s)