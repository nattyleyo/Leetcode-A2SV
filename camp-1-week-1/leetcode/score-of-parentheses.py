class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        # parent = {')':'('}
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(score)
                score = 0
            else:
                popped = stack.pop()
                score = popped + max( 1, 2*score)
        return score