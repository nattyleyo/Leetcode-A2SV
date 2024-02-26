class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        n = len(s)
        count = 0
        for i in range(n):
            if stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
                count = count-1 if count > 0 else 0
            else:
                count += 1
                stack.append(s[i])
        return count
            