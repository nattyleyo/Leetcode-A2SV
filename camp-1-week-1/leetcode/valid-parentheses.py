class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '{':'}',
            '[':']',
            '(':')'
        }
        for i in range(len(s )):
           #([{
            if s[i] in brackets:
                stack.append(s[i])
            elif len(stack) == 0 or s[i] != brackets[stack.pop()]:
                return False
        return len(stack) == 0