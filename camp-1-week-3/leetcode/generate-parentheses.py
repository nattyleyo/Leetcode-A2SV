class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path,openBr,closeBr):
            if openBr == n and openBr == closeBr:
                res.append(''.join(path))
                return
        
            if openBr < n:
                path.append('(')
                backtrack( path,openBr+1,closeBr)
                path.pop()
            if closeBr < openBr:
                path.append(')')
                backtrack(path,openBr,closeBr+1)
                path.pop()
        backtrack([],0,0)
        # print(res)
        return res
            